# ARKit VIO data parser
def loadVIO(filename):
    # Load the VIO txt file
    ARK = [x.strip() for x in open(filename, "r")]
    X = []; Y = []; Z = []; PITCH = []; YAW = []; ROLL = []; STATUS = []
    for idx in range(0, len(ARK)):
        if ARK[idx].isdigit():
            ind = int(ARK[idx])
            [x, y, z] = [float(x) for x in ARK[idx+4].split(',')]
            [pitch, yaw, roll] = [float(x) for x in ARK[idx+5].split('(')[1].strip(')').split(',')]
            normalStatus = ARK[idx+2] == 'normal'
            X.append(x)
            Y.append(y)
            Z.append(z)
            PITCH.append(pitch)
            YAW.append(yaw)
            ROLL.append(roll)
            STATUS.append(normalStatus)
    return X, Y, Z, PITCH, YAW, ROLL, STATUS
