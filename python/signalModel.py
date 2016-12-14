import os
import glob
import re

from Utils import getLimitsFromFile

class SignalModel:
    def __init__(self, path):
        """
        Initalise:
        * _path = stats output for this signal model
        * _model = name of signal model (taken from the path)
        """
        path = path.replace('\n','')
        if path[-1] == '/': path = path[:-1]
        if not os.path.exists(path):
            assert RuntimeError("Cannot find:", path)

        self._path = path
        self._model = path.split('/')[-1]

    def GetMasses(self):
        """
        Returns a tuple of (Mphi, Mchi) takes from the signal model name
        """
        return map(int, re.findall('(?<=M.hi-)[0-9]+', self._model))

    def GetExpLimits(self, jetCat="all"):
        """
        Read the limits from the file defined using fileTemplate
        """
        fileTemplate = "higgsCombine*_mht_*_exp.*.root"
        for limitFile in glob.glob(self._path+'/'+fileTemplate):
            if jetCat == "all": jetCat = "mht_card"
            if jetCat not in limitFile: continue
            limitList = getLimitsFromFile(limitFile)
        else:
            assert RuntimeError("Could not find limit for", self._model)
        if len(limitList) != 5: return {}
        limitDict = {
                "Down2" : limitList[0],
                "Down1" : limitList[1],
                "Med"   : limitList[2],
                "Up1"   : limitList[3],
                "Up2"   : limitList[4],
                }
        return limitDict
