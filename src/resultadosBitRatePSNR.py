# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="daniel"
__date__ ="$28/05/2010 15:42:00$"

if __name__ == "__main__":
    print "Hello World"

class ResultadosBitRatePSNR():

	def __init__(self,pathFile):
		self.pathFile = pathFile
		self.buff = []

	def createFile(self):
		fpResults = open(self.pathFile,'w')
		for i in range(0, len(self.buff)):
			fpResults.write(self.buff[i])
		fpResults.close()

	def writeLine(self,line):
		self.buff.insert((len(self.buff)),line)
