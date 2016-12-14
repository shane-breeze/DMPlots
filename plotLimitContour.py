import numpy as np
import optparse
from scipy import interpolate as spInterp

from signalModelCollection import SignalModelCollection

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-p", "--path", default=".", help="Path with stats output")
    parser.add_option("-s", "--model_selection", default="DMA", help="Model selection")
    options, args = parser.parse_args()
    return options

def createSignalModelCollection(path, model_selection):
    selection = [(model_selection)]
    return SignalModelCollection(path, selection)

def addLimitsToNumpyArray(signalModel, dictNumpyArray, limitRange=(0.,99999.)):
    expDict = signalModel.GetExpLimits()
    if len(expDict.keys()) == 0:
        print "Warning: Limits for "+signalModel._model+" not found!"
        return False
    if expDict['Med'] < limitRange[0] and expDict['Med'] > limitRange[1]:
        print "Limit for "+signalModel._model+" outside of range"
        return False
    masses = signalModel.GetMasses()
    for key, value in expDict.iteritems():
        if key not in dictNumpyArray.keys():
            dictNumpyArray[key] = np.array( [[masses[0], masses[1], value]] )
        else:
            dictNumpyArray[key] = np.append( dictNumpyArray[key], [[masses[0], masses[1], value]], axis=0 )
    return True

def Interpolate(data, method='linear', nConts=1000):
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]

    xi = np.linspace(x.min(), x.max(), nConts)
    yi = np.linspace(y.min(), y.max(), nConts)
    xi, yi = np.meshgrid(xi,yi)
    zi = spInterp.griddata( (x,y), z, (xi,yi), method=method)

    return xi, yi, zi

if __name__ == "__main__":
    options = parse_args()
    signalModelCollection = createSignalModelCollection(options.path, options.model_selection)

    expDictNumpy = {}
    for signalModel in signalModelCollection:
        addLimitsToNumpyArray(signalModel, expDictNumpy, limitRange=(0.,5.))

    expContourDict = {}
    for key, values in expDictNumpy.iteritems():
        expContourDict[key] = Interpolate(values)
