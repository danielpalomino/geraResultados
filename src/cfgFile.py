# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "daniel"
__date__ = "$21/05/2010 21:41:27$"

class CfgFile:

	def __init__(self, cfg_file, video):
		self.video = video
		self.cfg_file = cfg_file
		self.path = './'
		self.buff = self.getCfgRef(cfg_file)
		self.setVideo()

	def createFile(self):
		self.fp = self.openFile()
		for line in self.buff:
			self.fp.write(line)
		self.closeFile()

	def getCfgRef(self, cfgRef):
		fpRef = open(cfgRef, 'r')
		buff = fpRef.readlines()
		fpRef.close()
		return buff

	def getFileName(self):
		lst = self.cfg_file.split('/')
		return '../cfgFiles/' + lst[-1][:-4] + self.video[:-4] + '.cfg'

	def getVideoName(self):
		return self.video[:-12]

	def openFile(self):
		return open(self.getFileName(), 'w')

	def closeFile(self):
		self.fp.close()

	def setVideo(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('InputFile') != -1:
				lstword = self.buff[i].split()
				lstword[2] = '"' + '../videos/' + str(self.video) + '"'
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setResolution(self, width, height):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('SourceWidth') != -1 or self.buff[i].find('OutputWidth') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(width)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp
			if self.buff[i].find('SourceHeight') != -1 or self.buff[i].find('OutputHeight') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(height)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setFrameRate(self,frameRate):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('FrameRate') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(frameRate) + '.0'
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setNumberReferenceFrames(self,numberReferenceFrames):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('NumberReferenceFrames') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(numberReferenceFrames)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def disableIntraInInter(self,boolean):
	    for i in range(0, len(self.buff)):
		if self.buff[i].find('DisableIntraInInter') != -1:
		    lstword = self.buff[i].split()
		    lstword[2] = str(boolean)
		    temp = ''
		    for elem in lstword:
			temp = temp + elem + ' '
		    temp = temp + '\n'
		    self.buff[i] = temp

	def setIntraPeriod(self,period):
	    for i in range(0, len(self.buff)):
		if self.buff[i].find('I-pictures') != -1 and self.buff[i].find('IntraPeriod') != -1:
		    lstword = self.buff[i].split()
		    lstword[2] = str(period)
		    temp = ''
		    for elem in lstword:
			temp = temp + elem + ' '
		    temp = temp + '\n'
		    self.buff[i] = temp

	#metodo manda os arquivos gerados pela codificacao para uma outra pasta
	def setPathFiles(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('TraceFile') != -1 or self.buff[i].find('ReconFile') != -1 or self.buff[i].find('OutputFile') != -1 or self.buff[i].find('StatsFile') != -1 or self.buff[i].find('LeakyBucketParamFile') != -1 or self.buff[i].find('LeakyBucketRateFile') != -1:
				lstword = self.buff[i].split()
				lstword[2] = lstword[2][:1] + '../filesCodification/' + lstword[2][1:]
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def enableI16MB(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('DisableIntra16x16') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(0)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def enableI4MB(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('DisableIntra4x4') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(0)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def enableIPCM(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('EnableIPCM') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def disableI16MB(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('DisableIntra16x16') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def disableI4MB(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('DisableIntra4x4') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def disableIPCM(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('EnableIPCM') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(0)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setRDOoff(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('RDOptimization') != -1 and self.buff[i].find('rd-optimized') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(0)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setRDOon(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('RDOptimization') != -1 and self.buff[i].find('rd-optimized') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setI16RDOon(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('I16RDOpt') != -1 :
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setSADdistortion(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('MEDistortionFPel') != -1 or self.buff[i].find('MEDistortionHPel') != -1 or self.buff[i].find('MEDistortionQPel') != -1 or self.buff[i].find('MDDistortion') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(0)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setSSEdistortion(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('MEDistortionFPel') != -1 or self.buff[i].find('MEDistortionHPel') != -1 or self.buff[i].find('MEDistortionQPel') != -1 or self.buff[i].find('MDDistortion') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(1)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setSATDdistortion(self):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('MEDistortionFPel') != -1 or self.buff[i].find('MEDistortionHPel') != -1 or self.buff[i].find('MEDistortionQPel') != -1 or self.buff[i].find('MDDistortion') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(2)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setNumberOfFrames(self, numberOfFrames):
		for i in range(0, len(self.buff)):
			if self.buff[i].find('FramesToBeEncoded') != -1 and self.buff[i].find('Number of frames to be coded') != -1:
				lstword = self.buff[i].split()
				lstword[2] = str(numberOfFrames)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp

	def setQP(self, QP):
		for i in range(0, len(self.buff)):
			if (self.buff[i].find('QPISlice') != -1 and self.buff[i].find('Quant.') != -1) or (self.buff[i].find('QPPSlice') != -1 and self.buff[i].find('Quant.') != -1):
				lstword = self.buff[i].split()
				lstword[2] = str(QP)
				temp = ''
				for elem in lstword:
					temp = temp + elem + ' '
				temp = temp + '\n'
				self.buff[i] = temp
