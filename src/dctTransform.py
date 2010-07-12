import os
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="daniel"
__date__ ="$24/05/2010 21:17:36$"

class DCTTransform:

    def __init__(self,runableFile):
        self.fp = runableFile

    def run(self,originalBlocksFile,outDCTFile):
        cmd = self.fp + ' < ' + originalBlocksFile + ' > ' + outDCTFile
        os.system(cmd)
