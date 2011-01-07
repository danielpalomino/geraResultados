# CLASSE QUE DEFINE A HEURISTICA QUE AVALIA ELEMENTOS DA BORDA
# DO BLOCO 16X16 GERADOS PELA DCT

__author__ = "daniel"
__date__ = "$24/05/2010 21:27:35$"

I4MB = 9
I16MB = 10

class FileModes:

    def __init__(self, pathDCTfile):
        self.dctFile = pathDCTfile
        self.outFile = '../filesCoderHeuristic/ourModes.txt'
        self.homogeneityFile = '../filesCoderHeuristic/homogeneityMetricFile.txt'

    def geraHomogeneityMetricFile(self):
        fpDCTfile = open(self.dctFile, 'r')
        fpMetricFile = open(self.homogeneityFile, 'w')

        fpDCTfile.seek(0, 2)
        size = fpDCTfile.tell()
        fpDCTfile.seek(0, 0)

        i = 0
        metrica = 0
        while fpDCTfile.tell() < size:

            if((i % 16) == 15):
                fpMetricFile.write(str(metrica) + '\n')
                metrica = 0

            coefList = fpDCTfile.readline().split('\t')
            for coef in coefList:
                metrica += abs(int(coef))
            i = i + 1

        fpMetricFile.close()
        fpDCTfile.close()

    def geraOurModes(self, TH):
        fpMetricFile = open(self.homogeneityFile,'r')
        fpHeuristicModes = open(self.outFile, 'w')

        fpMetricFile.seek(0,2)
	size = fpMetricFile.tell()
	fpMetricFile.seek(0,0)

        while fpMetricFile.tell() < size:

            metrica = fpMetricFile.readline()
            if(int(metrica) < TH):
                fpHeuristicModes.write(str(I16MB) + '\n')
            else:
                fpHeuristicModes.write(str(I4MB) + '\n')

        fpHeuristicModes.close()
        fpMetricFile.close()
