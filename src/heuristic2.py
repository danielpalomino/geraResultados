# CLASSE QUE DEFINE A HEURISTICA QUE AVALIA ELEMENTOS DENTRO DE UMA
# DETERMINADA AREA DOS COEFICIENTES DO BLOCO 16X16 GERADOS PELA DCT
__author__ = "daniel"
__date__ = "$04/06/2010 17:01:13$"

if __name__ == "__main__":
    print "Hello World"

class Heuristic2:

    def __init__(self, TH_COEF, TH, SQUARE_SIZE, pathBlocksFile):
        self.TH_COEF = TH_COEF
        self.TH = TH
        self.SQUARE_SIZE = SQUARE_SIZE
        self.blocksFile = pathBlocksFile
        self.outFile = '../filesCoderHeuristic2/ourModes.txt'

    def geraFile(self):
        self.fpOriginalBlocks = open(self.blocksFile, 'r')
        buff = self.fpOriginalBlocks.readlines()
        self.fpOriginalBlocks.close()
        self.fpHeuristicModes = open(self.outfile, 'w')

        metrica = 0

        for i in range(0, len(buff)):
            
            if(i % 16 == 0 and i != 0):
                if(metrica < self.TH):
                    self.fpHeuristicModes.write(str(I16MB) + '\n')
                else:
                    self.fpHeuristicModes.write(str(I4MB) + '\n')
                metrica = 0

            coefList = buff[i].split('\t')

            
            for k in range(0, len(coefList)):
                #VERIFICA SE É A PRIMEIRA LINHA ONDE ESTAH O ELEMENTO DC E SE O ELEMENTO ESTAH DENTRO DO QUADRADO DEFINIDO
                if(i % 16 == 0 and k != 0 and k < SQUARE_SIZE):
                    if(coefList[k] < TH_COEF):
                        metrica += 1
                else:
                    #DEMAIS LINHAS E A DIAGONAL DO QUADRADO QUE DEFINE QUAIS ELEMENTOS SERÃO AVALIADOS
                    if(i % 16 < SQUARE_SIZE and k < (SQUARE_SIZE - i%16)):
                        if(coefList[k] < TH_COEF):
                            metrica +=1

            self.fpHeuristicModes.close()