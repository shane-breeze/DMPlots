import os, sys
import ROOT as r
r.gROOT.SetBatch(True)
r.PyConfig.IgnoreCommandLineOptions = True


def getListModels(dcDir):
    dcDir = os.path.abspath(dcDir)
    models = []
    if os.path.exists(dcDir+"/signalModelsNoFail.txt"):
        with open(dcDir+"/signalModelsNoFail.txt") as f:
            models = f.read().splitlines()
    elif os.path.exists(dcDir+"/signalModels.txt"):
        with open(dcDir+"/signalModels.txt") as f:
            models = f.read().splitlines()
    else:
        print "[getListModels] No way of getting the list of models!"
        sys.exit(1)

    return models


def getListJets(dcDir,ussr=True):
    dcDir = os.path.abspath(dcDir)
    cats = []
    if os.path.exists(dcDir+"/configuration.txt"):
        with open(dcDir+"/configuration.txt") as f:
            for aLine in f:
                if ussr:
                    if "ussrCats" in aLine: cats = aLine.replace("ussrCats","").strip().split(",")
                else:
                    if "cats" in aLine: cats = aLine.replace("cats","").strip().split(",")
        cats = sorted(list(set([aCat.split("_")[1] for aCat in cats])))
    else:
        print "[getListJets] No way of getting the list of jet categories!"
        sys.exit(1)

    return cats


def getListBJets(dcDir,ussr=True):
    dcDir = os.path.abspath(dcDir)
    bjets = []
    if os.path.exists(dcDir+"/configuration.txt"):
        with open(dcDir+"/configuration.txt") as f:
            for aLine in f:
                if ussr:
                    if "ussrCats" in aLine: bjets = aLine.replace("ussrCats","").strip().split(",")
                else:
                    if "bjets" in aLine: bjets = aLine.replace("bjets","").strip().split(",")
        bjets   = sorted(list(set([aCat.split("_")[0] for aCat in bjets])))
    else:
        print "[getListBJets] No way of getting the list of categories!"
        sys.exit(1)

    return bjets


def getListBinVars(dcDir):
    dcDir = os.path.abspath(dcDir)
    binVars = []
    if os.path.exists(dcDir+"/configuration.txt"):
        with open(dcDir+"/configuration.txt") as f:
            for aLine in f:
                if "fourthDim" in aLine: binVars = aLine.replace("fourthDim","").strip().split(",")
    else:
        binVars = [""]
        # print "[getListBinVars] No way of getting the list of categories!"
        # sys.exit(1)

    return binVars


def getListHtBins(dcDir,ussr = True):
    dcDir = os.path.abspath(dcDir)
    htBins = []
    if os.path.exists(dcDir+"/configuration.txt"):
        with open(dcDir+"/configuration.txt") as f:
            for aLine in f:
                if ussr:
                    if "ussrHtBins" in aLine: htBins = aLine.replace("ussrHtBins","").strip().split(",")
                else:
                    if "htBins" in aLine: htBins = aLine.replace("htBins","").strip().split(",")
    else:
        print "[getListHtBins] No way of getting the list of categories!"
        sys.exit(1)

    return htBins


def getLimitTreeFromFile(fileName, verbose=False):
    tt = None

    if not isRootFileOk(fileName):
        print "[getLimitTreeFromFile] file does not exist or is corrupted.\n",fileName
        return None

    tf = r.TFile(fileName)

    for aKey in tf.GetListOfKeys():
        if aKey.GetName() == "limit": tt = tf.Get("limit")

    if not tt and verbose: print "[getLimitTreeFromFile] file does not contain the \"limit\" tree!\n",fileName
    return (tf,tt)


def getLimitsFromFile(fileName,strict=False, verbose=False):
    if not isRootFileOk(fileName):
        print "[getLimitsFromFile] ERROR: File {0} is corrupted or not existing".format(fileName)
        sys.exit()

    limit = []
    (tf,tt) = getLimitTreeFromFile(fileName,verbose)

    if tt:
        tt.SetBranchStatus("*",0)
        tt.SetBranchStatus("limit",1)
        iEntry = 0
        while tt.GetEntry(iEntry):
            iEntry += 1
            limit.append(tt.limit)
    elif strict:
        print "[getLimitsFromFile] ERROR: cannot get limit from file:\n",fileName
        sys.exit(1)
    else:
        if verbose: print "[getLimitsFromFile] WARNING: cannot get limit from file, returning empty limit array:\n",fileName

    return limit


def isRootFileOk(fileName):
    isOK = False
    if os.path.exists(os.path.abspath(fileName)):
        # r.gErrorIgnoreLevel=r.kError
        r.gErrorIgnoreLevel=r.kSysError
        tf = r.TFile(os.path.abspath(fileName),"READ")
        if not (tf.IsZombie() or tf.TestBit(r.TFile.kRecovered)): isOK = True
        tf.Close()

    return isOK
