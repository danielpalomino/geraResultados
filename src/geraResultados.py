# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "daniel"
__date__ = "$21/05/2010 21:40:33$"

from resultadosBitRatePSNR import ResultadosBitRatePSNR
from dctTransform import DCTTransform
from cfgFile import CfgFile
from coder import Coder
from fileModes import FileModes

#DEFINICOES
dct = '../DCT/dct'
outDCTFile = '../DCT/outDCT.txt'
cfgRef = '/home/daniel/NetBeansProjects/jm-heuristic/bin/encoder_baseline28.cfg'
coderNormal = '/home/daniel/NetBeansProjects/jm-normal/bin/lencod.exe'
coderHeuristic = '/home/daniel/NetBeansProjects/jm-heuristic/bin/lencod.exe'
resultsFile = '../Resultados/results.csv'
#VideoList = ['ROLLINGTOMATOES_1920x1080_25_orig_01.yuv']
VideoList = ['STATION2_1920x1080_25_orig_01.yuv',
'SUNFLOWER_1920x1080_25_orig_01.yuv',
'TRACTOR_1920x1080_25_orig_01.yuv',
'TRAFFIC_1920x1080_25_orig_01.yuv',
'MANINCAR_1920x1080_25_orig_01.yuv',
'PEDISTRIANAREA_1920x1080_25_orig_01.yuv',
'RIBERBED_1920x1080_25_orig_01.yuv',
'ROLLINGTOMATOES_1920x1080_25_orig_01.yuv',
'RUSHHOUR_1920x1080_25_orig_01.yuv']
#VideoList = ['FOREMAN_352x288_30_orig_01.yuv', 'BUS_352x288_30_orig_01.yuv', 'CITY_352x288_30_orig_01.yuv', 'FOOTBALL_352x288_30_orig_01.yuv', 'HARBOUR_352x288_30_orig_01.yuv', 'ICE_352x288_30_orig_02.yuv', 'SOCCER_352x288_30_orig_02.yuv', 'SOCCER_704x576_30_orig_02.yuv']
ListTH = []
ListTH.extend(range(0, 8000, 100))
#ListTH = [4000]
NUM_FRAMES = 10
ENABLE_I4MB = 1
ENABLE_I16MB = 0
RDO_ON = 1
QP = 28
SAD = 0
SSE = 1
SATD = 2
MDDistortion = SSE
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
	modes = FileModes(TH,outDCTFile)
	modes.geraFile()

def runCoderHeuristic(cfgFile):
	heuristicCoder = Coder(coderHeuristic)
	heuristicCoder.run(cfgFile)

def getHeuristicFileResults():
	fpResults = open('../filesCoderHeuristic/resultsPSNRBits.txt','r')
	return fpResults.readlines()

def getNormalFileResults():
	fpResults = open('../filesCoderNormal/resultsPSNRBits.txt','r')
	return fpResults.readlines()

def resultsIntra():
    cfgList = geraCfgs(VideoList)
    resultados = ResultadosBitRatePSNR(resultsFile)
    for cfg in cfgList:
	    resultados.writeLine(cfg.getVideoName() + '\n')
	    runCoderNormal(cfg.getFileName())

	    buff1 = getNormalFileResults()
	    for line in buff1:
			    resultados.writeLine('Normal, ' + 'RDO,' + line)

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

	    runDCT()
	    for TH in ListTH:
		    resultados.writeLine(str(TH) + ',')
		    geraOurModes(TH)
		    runCoderHeuristic(cfg.getFileName())
		    buff = getHeuristicFileResults()
		    for line in buff:
			    resultados.writeLine(line)

    resultados.createFile()

if __name__ == "__main__":
    resultsIntra()
    #main()
