# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="daniel"
__date__ ="$21/05/2010 21:45:15$"

import os

class Coder:
    
	def __init__(self,runableFile):
		self.fp = ''
		self.fp = runableFile

	def run(self,cfgFile):
		cmd = self.fp + ' -d ' + str(cfgFile)
		print cmd
		os.system(cmd)