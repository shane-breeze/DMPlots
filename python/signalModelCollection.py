import os
import re

from signalModel import SignalModel

class SignalModelCollection:
    def __init__(self, path, modelSelection=None):
        """
        Initialise:
        * _path = directory containing the signal model directories
        * _modelListFile = file name containing the list of signal models in
            _path
        * _modelSelection = list of tuples with regex strings for a model
            selection
        * _signalModels = list containing the SignalModel classes
        """

        if path[-1] == '/': path = path[:-1]
        if not os.path.exists(path):
            assert RuntimeError("Cannot find:", path)

        self._path = path
        self._modelListFile = "signalModelsNoFail.txt"
        self._modelSelection = modelSelection
        self._signalModels = self.FillModels()

    def __iter__(self):
        return iter(self._signalModels)

    def FillModels(self):
        """
        Open the _modelListFile in the _path directory to read all successful
        models. Creates a SignalModel class for each one, filling _signalModels
        """
        signalModelNames = open(self._path+'/'+self._modelListFile, 'r').readlines()
        signalModels = []
        for signalModelName in signalModelNames:
            if signalModelName == "" or signalModelName == None: continue
            signalModel = SignalModel(self._path+'/'+signalModelName)

            isInSelection = self.IsInSelection(signalModel)
            if isInSelection or len(self._modelSelection) == 0:
                signalModels.append(signalModel)
        else:
            assert RuntimeError("No models found in", self._path)
        return signalModels

    def IsInSelection(self, signalModel):
        """
        Selection criteria for models:
            self._modelSelection is a list of tuples:
            * All items in a tuple must be satisfied
            * Any item in the list must be satisfied
            Regex is used to see if there is a match
        """
        if self._modelSelection is None: return True
        modelName = signalModel._model
        isInSelection =\
            any([
                all([
                    re.search(item, modelName) != None
                    for item in selection
                    ])
                for selection in self._modelSelection
                ])
        return isInSelection
