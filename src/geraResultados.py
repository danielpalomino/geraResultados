# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "daniel"
__date__ = "$21/05/2010 21:40:33$"

from cfgFile import CfgFile
from coder import Coder
from dctTransform import DCTTransform
from fileModes import FileModes
from fileModesSADheuristic import FileModesSADheuristic
from resultadosBitRatePSNR import ResultadosBitRatePSNR

#DEFINICOES
dct = '../DCT/dct'
outDCTFile = '../DCT/outDCT.txt'
pathPredictedI16MB = '../filesCoderNormal/predictedI16MB.txt'
pathPredictedI4MB = '../filesCoderNormal/predictedI4MB.txt'
pathOriginalBlocks = '../filesCoderNormal/originalBlocks.txt'
cfgRef = '/home/daniel/NetBeansProjects/jm-normal/bin/encoder_baseline.cfg'
coderNormal = '/home/daniel/NetBeansProjects/jm-normal/bin/lencod.exe'
coderHeuristic = '/home/daniel/NetBeansProjects/jm-heuristic/bin/lencod.exe'
resultsFile = '../Resultados/results.csv'
VideoList = ['ICE_352x288_30_orig_02.yuv']
#VideoList = ['STATION2_1920x1080_25_orig_01.yuv',
#'SUNFLOWER_1920x1080_25_orig_01.yuv',
#'TRACTOR_1920x1080_25_orig_01.yuv',
#'TRAFFIC_1920x1080_25_orig_01.yuv',
#'MANINCAR_1920x1080_25_orig_01.yuv',
#'PEDISTRIANAREA_1920x1080_25_orig_01.yuv',
#'RIBERBED_1920x1080_25_orig_01.yuv',
#'ROLLINGTOMATOES_1920x1080_25_orig_01.yuv',
#'RUSHHOUR_1920x1080_25_orig_01.yuv']
#video = 'TRACTOR_1920x1080_25_orig_01.yuv'
#VideoList = ['FOREMAN_352x288_30_orig_01.yuv', 'BUS_352x288_30_orig_01.yuv', 'CITY_352x288_30_orig_01.yuv', 'FOOTBALL_352x288_30_orig_01.yuv', 'HARBOUR_352x288_30_orig_01.yuv', 'ICE_352x288_30_orig_02.yuv', 'SOCCER_352x288_30_orig_02.yuv', 'SOCCER_704x576_30_orig_02.yuv']
ListTH = []
ListTH.extend(range(0, 1000, 10))
#ListTH = [10,50]
NUM_FRAMES = 10
ENABLE_I4MB = 1
ENABLE_I16MB = 1
ENABLE_IPCM = 1
RDO_ON = 1
I16RDO = 1
QP = 28
#QPList = [12,25,38,51]
SAD = 0
SSE = 1
SATD = 2
MDDistortion = SAD
DISABLEINTRAININTER = 0
INTRAPERIOD = 1
NUMBEROFREFERENCEFRAMES = 4

def setCfgFile(cfgFile):
    if(ENABLE_I4MB):
	cfgFile.enableI4MB()
    else:
	cfgFile.disableI4MB()
    if(ENABLE_I16MB):
	cfgFile.enableI16MB()
    else:
	cfgFile.disableI16MB()
    if(RDO_ON):
	cfgFile.setRDOon()
    else:
	cfgFile.setRDOoff()
    if(I16RDO):
	cfgFile.setI16RDOon()
    if(ENABLE_IPCM):
	cfgFile.enableIPCM()
    else:
	cfgFile.disableIPCM()
    if(MDDistortion == SAD):
	cfgFile.setSADdistortion()
    else:
	if(MDDistortion == SSE):
	    cfgFile.setSSEdistortion()
	else:
	    cfgFile.setSATDdistortion()

    cfgFile.disableIntraInInter(DISABLEINTRAININTER)
    cfgFile.setIntraPeriod(INTRAPERIOD)
    videoName = cfgFile.getVideoName()
    list = videoName.split("_")
    listRes = list[1].split("x")
    width = listRes[0]
    height = listRes[1]
    cfgFile.setResolution(width, height)

	
    cfgFile.setFrameRate(list[2])
    cfgFile.setNumberReferenceFrames(NUMBEROFREFERENCEFRAMES)
	
    cfgFile.setPathFiles()
    cfgFile.setNumberOfFrames(NUM_FRAMES)
    cfgFile.setQP(QP)
    cfgFile.createFile()



def geraCfgs(videos):
    cfgList = []
    for video in videos:
	cfgFile = CfgFile(cfgRef, video)
	setCfgFile(cfgFile)
	cfgList.append(cfgFile)
    return cfgList

def runCoderNormal(cfgFile):
    normalCoder = Coder(coderNormal)
    normalCoder.run(cfgFile)

def runDCT():
    transform = DCTTransform(dct)
    transform.run('../filesCoderNormal/originalBlocks.txt', outDCTFile)

def geraOurModes(TH):
    modes = FileModes(TH, outDCTFile)
    modes.geraFile()

def geraOurModesSAD(TH):
    modes = FileModesSADheuristic(TH, pathResidualI4MB, pathResidualI16MB)
    modes.geraFile()

def runCoderHeuristic(cfgFile):
    heuristicCoder = Coder(coderHeuristic)
    heuristicCoder.run(cfgFile)

def getHeuristicFileResults():
    fpResults = open('../filesCoderHeuristic/resultsPSNRBits.txt', 'r')
    buff = fpResults.readlines()
    fpResults.close()
    return buff

def getNormalFileResults():
    fpResults = open('../filesCoderNormal/resultsPSNRBits.txt', 'r')
    buff = fpResults.readlines()
    fpResults.close()
    return buff

def resultsIntra():
    cfgList = geraCfgs(VideoList)
    resultados = ResultadosBitRatePSNR(resultsFile)
    for cfg in cfgList:
	resultados.writeLine(cfg.getVideoName() + '\n')
	runCoderNormal(cfg.getFileName())

	buff1 = getNormalFileResults()
	for line in buff1:
	    resultados.writeLine('RDO-off,SAD,16x16' + line)

    resultados.createFile()

def claudioSimulation():
    resultados = ResultadosBitRatePSNR(resultsFile)
    for qp in QPList:
	cfgFile = CfgFile(cfgRef, video)
	setCfgFile(cfgFile, qp)
	resultados.writeLine(cfgFile.getVideoName() + '\n')
	resultados.writeLine(str(qp) + ',')
	runCoderNormal(cfgFile.getFileName())

	buff1 = getNormalFileResults()
	for line in buff1:
	    resultados.writeLine(line)

    resultados.createFile()

def main():
    cfgList = geraCfgs(VideoList)
    resultados = ResultadosBitRatePSNR(resultsFile)
    for cfg in cfgList:
	resultados.writeLine(cfg.getVideoName() + '\n')
	runCoderNormal(cfg.getFileName())

	buff1 = getNormalFileResults()

	for line in buff1:
	    resultados.writeLine('Normal,' + line)

#	    runDCT()
#	    for TH in ListTH:
#		    print 'Rodando para o Threshold ' + str(TH)
#		    resultados.writeLine(str(TH) + ',')
#		    geraOurModes(TH)
#		    runCo#derHeuristic(cfg.getFileName())
#		    buff = getHeuristicFileResults()
#		    for line in buff:
#			    resultados.writeLine(line)

    resultados.createFile()
    
def heuristicSAD():
    cfgList = geraCfgs(VideoList)
    resultados = ResultadosBitRatePSNR(resultsFile)
    for cfg in cfgList:
	resultados.writeLine(cfg.getVideoName() + '\n')
	runCoderNormal(cfg.getFileName())
	
	buff = getNormalFileResults()
	for line in buff:
	    resultados.writeLine('Normal,' + line)

	modes = FileModesSADheuristic(pathPredictedI4MB, pathPredictedI16MB, pathOriginalBlocks)
	print 'gerando residuos...'
	modes.geraResidualFiles()
	print 'gerando sads...'
	modes.geraSADfiles()
	print 'gerando diferencas...'
	modes.splitSADdifferences()

	for TH in ListTH:
	    print 'Rodando para o Threshold ' + str(TH)
	    resultados.writeLine(str(TH) + ',')	    
	    print 'gerando our modes...'
	    modes.geraOurModesFile(TH)
	    runCoderHeuristic(cfg.getFileName())
	    buff1 = getHeuristicFileResults()
	    for line in buff1:
		resultados.writeLine(line)

    resultados.createFile()
    
if __name__ == "__main__":
#    resultsIntra()
#    main()
#    claudioSimulation()
    heuristicSAD()
