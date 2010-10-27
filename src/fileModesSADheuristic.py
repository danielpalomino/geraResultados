# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="daniel"
__date__ ="$19/10/2010 13:50:58$"


I4MB = 9
I16MB = 10

class FileModesSADheuristic:

    def __init__(self, pathPredictedI4MB, pathPredictedI16MB, pathOriginalBlocks):
		self.originalBlock = pathOriginalBlocks
		self.predictedI4MB = pathPredictedI4MB
		self.predictedI16MB = pathPredictedI16MB
		self.residualI4MB =  '../filesCoderNormal/residualI4MB.txt'
		self.residualI16MB =  '../filesCoderNormal/residualI16MB.txt'
		self.sadI4MB = '../filesCoderNormal/sadI4MB.txt'
		self.sadI16MB = '../filesCoderNormal/sadI16MB.txt'
		self.sadDifference = '../filesCoderNormal/sadDifferences.txt'
		self.sadI16MBDifference = '../filesCoderNormal/sadI16MBDifferences.csv'
		self.sadI4MBDifference = '../filesCoderNormal/sadI4MBDifferences.csv'
		self.allIntraModes = '../filesCoderNormal/allIntraModes.txt'
		self.outFile = '../filesCoderHeuristic/ourModes.txt'

    def sad(self, residual):
	sad = 0
	for line in residual:
	    buff = line.split('\t')
	    for i in range(0,len(buff)-1):
		sad = sad + abs(int(buff[i]))
	return sad

    def geraResidualFiles(self):
	fpOriginal = open(self.originalBlock,'r')
        fpI4MB = open(self.predictedI4MB,'r')
	fpI16MB = open(self.predictedI16MB,'r')
	self.fpI4MBresidual = open(self.residualI4MB,'w')
	self.fpI16MBresidual = open(self.residualI16MB,'w')
	
	fpOriginal.seek(0,2)
	size = fpOriginal.tell()
	fpOriginal.seek(0,0)
	
	while fpOriginal.tell() < size:
	    blockI4MB = fpI4MB.readline().split('\t')
	    blockI16MB = fpI16MB.readline().split('\t')
	    blockOriginal = fpOriginal.readline().split('\t')

	    for i in range(0,len(blockOriginal)-1):
		a = int(blockI4MB[i])
		b = int(blockI16MB[i])
		c = int(blockOriginal[i])
		self.fpI4MBresidual.write(str(c-a) + '\t')
		self.fpI16MBresidual.write(str(c-b) + '\t')

	    self.fpI4MBresidual.write('\n')
	    self.fpI16MBresidual.write('\n')

	self.fpI16MBresidual.close()
	self.fpI4MBresidual.close()
	fpOriginal.close()
	fpI16MB.close()
	fpI4MB.close()

    def geraSADfiles(self):

	fpI4MBresidual = open(self.residualI4MB,'r')
	fpI16MBresidual = open(self.residualI16MB,'r')
	fpI4MBsad = open(self.sadI4MB,'w')
	fpI16MBsad = open(self.sadI16MB,'w')
	fpSADdifferences = open(self.sadDifference,'w')
	
	i = 0
	blockI4MB = []
	blockI16MB = []

	fpI4MBresidual.seek(0,2)
	size = fpI4MBresidual.tell()
	fpI4MBresidual.seek(0,0)

	while fpI4MBresidual.tell() < size:
	    
	    blockI4MB.append(fpI4MBresidual.readline())
	    blockI16MB.append(fpI16MBresidual.readline())

	    if((i%16) == 15):
		sadI4MB = self.sad(blockI4MB)
		sadI16MB = self.sad(blockI16MB)
		fpI4MBsad.write(str(sadI4MB) + '\n')
		fpI16MBsad.write(str(sadI16MB) + '\n')
		fpSADdifferences.write(str(abs(sadI16MB - sadI4MB)) + '\n')
		blockI4MB = []
		blockI16MB = []

	    i = i + 1

	fpI4MBsad.close()
	fpI16MBsad.close()
	fpSADdifferences.close()
	fpI4MBresidual.close()
	fpI16MBresidual.close()

    def splitSADdifferences(self):
	fpSADdifferences = open(self.sadDifference,'r')
	fpallIntraModes = open(self.allIntraModes,'r')
	fpI16MBSADdifferences = open(self.sadI16MBDifference,'w')
	fpI4MBSADdifferences = open(self.sadI4MBDifference,'w')

	fpSADdifferences.seek(0,2)
	size = fpSADdifferences.tell()
	fpSADdifferences.seek(0,0)

	while fpSADdifferences.tell() < size:
	    mode = fpallIntraModes.readline()
	    if(int(mode) == I16MB):
		fpI16MBSADdifferences.write(fpSADdifferences.readline())
	    else:
		fpI4MBSADdifferences.write(fpSADdifferences.readline())
		
	fpI16MBSADdifferences.close()
	fpI4MBSADdifferences.close()
	fpSADdifferences.close()
	fpallIntraModes.close()




    def geraOurModesFile(self,TH):
	fpSADdifferences = open(self.sadDifference,'r')
	self.fpHeuristicModes = open(self.outFile,'w')
	
	fpSADdifferences.seek(0,2)
	size = fpSADdifferences.tell()
	fpSADdifferences.seek(0,0)
	i = 0
	while fpSADdifferences.tell() < size:

	    sad = fpSADdifferences.readline()
	    
	    if((int(sad)) < (TH)):
		self.fpHeuristicModes.write(str(I16MB) + '\n')
	    else:
		self.fpHeuristicModes.write(str(I4MB) + '\n')

	    i = i + 1
	self.fpHeuristicModes.close()
	    