__author__ = "daniel"
__date__ = "$11/06/2010 16:25:08$"

from coder import Coder
from cfgFile import CfgFile
from geraResultados import *

cfgRef = '/home/daniel/NetBeansProjects/jm-normal/bin/encoder_baseline.cfg'
coderNormal = '/home/daniel/NetBeansProjects/jm-normal/bin/lencod.exe'
#VideoList = ['STATION2_1920x1080_25_orig_01.yuv']
#VideoList = ['FOREMAN_352x288_30_orig_01.yuv', 'BUS_352x288_30_orig_01.yuv', 'CITY_352x288_30_orig_01.yuv', 'FOOTBALL_352x288_30_orig_01.yuv', 'HARBOUR_352x288_30_orig_01.yuv', 'ICE_352x288_30_orig_02.yuv', 'SOCCER_352x288_30_orig_02.yuv', 'SOCCER_704x576_30_orig_02.yuv']
VideoList = ['STATION2_1920x1080_25_orig_01.yuv',
'SUNFLOWER_1920x1080_25_orig_01.yuv',
'TRACTOR_1920x1080_25_orig_01.yuv',
'TRAFFIC_1920x1080_25_orig_01.yuv',
'MANINCAR_1920x1080_25_orig_01.yuv',
'PEDISTRIANAREA_1920x1080_25_orig_01.yuv',
'RIBERBED_1920x1080_25_orig_01.yuv',
'ROLLINGTOMATOES_1920x1080_25_orig_01.yuv',
'RUSHHOUR_1920x1080_25_orig_01.yuv']

PSKIP = 0
P16x16 = 1
P16x8 = 2
P8x16 = 3
SMB8x8 = 4
SMB8x4 = 5
SMB4x8 = 6
SMB4x4 = 7
P8x8 = 8
I4MB = 9
I16MB = 10

def geraCfgs(videos):
    cfgList = []
    for video in videos:
	cfgFile = CfgFile(cfgRef, video)
	setCfgFile(cfgFile)
	cfgList.append(cfgFile)
    return cfgList

def runCoder(cfgFile):
    coder = Coder(coderNormal)
    coder.run(cfgFile)

def writeResultsFile(list,blockType,countType,countAll):
    list.append(blockType+': ')
    list.append(str(countType) + ' - ')
    list.append(str(float(countType)/float(countAll)*100)+'%'+'\n')

def calculaNumberOfModes():
    fpModes = open('/home/daniel/NetBeansProjects/GeraResultados/filesCoderNormal/allIntraModes.txt', 'r')

    countPSKIP = 0
    countP16x16 = 0
    countP16x8 = 0
    countP8x16 = 0
    countSMB8x8 = 0
    countSMB8x4 = 0
    countSMB4x8 = 0
    countSMB4x4 = 0
    countP8x8 = 0
    countI4MB = 0
    countI16MB = 0

    buff = fpModes.readlines()
    countAll = len(buff)


    fpModes.seek(0,2)
    size = fpModes.tell()
    fpModes.seek(0,0)

    while fpModes.tell() < size:
        line = fpModes.readline()
        
	if int(line) == PSKIP:
	    countPSKIP += 1
	elif int(line) == P16x16:
	    countP16x16 += 1
	elif int(line) == P16x8:
	    countP16x8 += 1
	elif int(line) == P8x16:
	    countP8x16 += 1
	elif int(line) == SMB8x8:
	    countSMB8x8 += 1
	elif int(line) == SMB8x4:
	    countSMB8x4 += 1
	elif int(line) == SMB4x8:
	    countSMB4x8 += 1
	elif int(line) == SMB4x4:
	    countSMB4x4 += 1
	elif int(line) == P8x8:
	    countP8x8 += 1
	elif int(line) == I4MB:
	    countI4MB += 1
	else:
	    countI16MB += 1

    results = []

    results.append("\n")

    results.append('Total Macroblocks: ')
    results.append(str(countAll) + '\n')

    writeResultsFile(results, 'PSKIP', countPSKIP, countAll)
    writeResultsFile(results, 'P16x16', countP16x16, countAll)
    writeResultsFile(results, 'P16x8', countP16x8, countAll)
    writeResultsFile(results, 'P8x16', countP8x16, countAll)
    writeResultsFile(results, 'SMB8x8', countSMB8x8, countAll)
    writeResultsFile(results, 'SMB8x4', countSMB8x4, countAll)
    writeResultsFile(results, 'SMB4x8', countSMB4x8, countAll)
    writeResultsFile(results, 'SMB4x4', countSMB4x4, countAll)
    writeResultsFile(results, 'P8x8', countP8x8, countAll)
    writeResultsFile(results, 'I4MB', countI4MB, countAll)
    writeResultsFile(results, 'I16MB', countI16MB, countAll)

    fpModes.close()

    return results


def main():
    cfgList = geraCfgs(VideoList)
    fp_Results = open('/home/daniel/NetBeansProjects/GeraResultados/Resultados/allModesResults.txt','w')
    
    for cfg in cfgList:
	runCoder(cfg.getFileName())
	
        buff = calculaNumberOfModes()
        fp_Results.write(cfg.getVideoName())
        for line in buff:            
            fp_Results.write(line)
    
    fp_Results.close()



if __name__ == "__main__":
    main()

