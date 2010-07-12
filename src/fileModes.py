# CLASSE QUE DEFINE A HEURISTICA QUE AVALIA ELEMENTOS DA BORDA
# DO BLOCO 16X16 GERADOS PELA DCT

__author__ = "daniel"
__date__ = "$24/05/2010 21:27:35$"

I4MB = 9
I16MB = 10

class FileModes:

    def __init__(self, TH, pathBlocksFile):
		self.TH = TH
		self.blocksFile = pathBlocksFile
		self.outFile = '../filesCoderHeuristic/ourModes.txt'


    def geraFile(self):
        self.fpOriginalBlocks = open(self.blocksFile, 'r')
        buff = self.fpOriginalBlocks.readlines()
        self.fpOriginalBlocks.close()
        self.fpHeuristicModes = open(self.outFile, 'w')

        metrica = 0
        for i in range(0, len(buff)):

            if(i % 16 == 0 and i != 0):
                if(metrica < self.TH):
                    self.fpHeuristicModes.write(str(I16MB) + '\n')
                else:
                    self.fpHeuristicModes.write(str(I4MB) + '\n')
                metrica = 0


            coefList = buff[i].split('\t')
            for coef in coefList:
                metrica += abs(int(coef))

        self.fpHeuristicModes.close()
