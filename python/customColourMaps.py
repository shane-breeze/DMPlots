import matplotlib.colors as mcol

def makeColorMap(stops, red, green, blue, name=""):
    uRed = []
    uGreen = []
    uBlue = []
    for i, stop in enumerate(stops):
        if i is 0:
            uRed.append( (stop, 0., red[i]) )
            uGreen.append( (stop, 0., green[i]) )
            uBlue.append( (stop, 0., blue[i]) )
        elif i is len(stops)-1:
            uRed.append( (stop, red[i], 1.) )
            uGreen.append( (stop, green[i], 1.) )
            uBlue.append( (stop, blue[i], 1.) )
        else:
            uRed.append( (stop, red[i], red[i]) )
            uGreen.append( (stop, green[i], green[i]) )
            uBlue.append( (stop, blue[i], blue[i]) )
    cdict = {'red' : uRed, 'green' : uGreen, 'blue' : uBlue}
    return mcol.LinearSegmentedColormap(name, cdict)

def birdMap():
    stops = [0.0000, 0.1250, 0.2500, 0.3750, 0.5000, 0.6250, 0.7500, 0.8750, 1.0000]
    red   = [0.2082, 0.0592, 0.0780, 0.0232, 0.1802, 0.5301, 0.8186, 0.9956, 0.9764]
    green = [0.1664, 0.3599, 0.5041, 0.6419, 0.7178, 0.7492, 0.7328, 0.7862, 0.9832]
    blue  = [0.5293, 0.8684, 0.8385, 0.7914, 0.6425, 0.4662, 0.3499, 0.1968, 0.0539]

    return makeColorMap(stops, red, green, blue, name='bird')

def exclusionMap():
    stops = [0.00, 0.34, 0.61, 0.84, 1.00]
    red   = [0.00, 0.00, 0.87, 1.00, 0.51]
    green = [0.00, 0.81, 1.00, 0.20, 0.00]
    blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

    return makeColorMap(stops, red, green, blue, name='exclusion')
