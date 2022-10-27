import numpy as np 

def get_position(file: str, indexes: list, read: bool=True, geom: bool=False):
    '''
    From a file get the positional vector of defined atoms

    param: file: xtz filename or str of a xyz file
    param: indexes: list of indexes *starting from 1
    param: read: if the file prm is as filename
    param: geom: xyzfile 
    '''

    if read:
        with open(file) as f:
            fl = f.readlines()[2:]
    elif not geom:
        fl = file.split('\n')[1:]
    else:
        fl = file.split('\n')[2:]

    return np.array([fl[int(i)-1].split()[1:] for i in indexes], dtype=np.float64)


def dihedral(p) -> float:
    '''
    Evaluate the dihedral angle between 4 atoms

    param: p: 4 positional arraies
    return: float
    '''
    p0 = p[0]
    p1 = p[1]
    p2 = p[2]
    p3 = p[3]
    b0 = -1.0*(p1 - p0)
    b1 = p2 - p1
    b2 = p3 - p2
    b1 /= np.linalg.norm(b1)
    v = b0 - np.dot(b0, b1)*b1
    w = b2 - np.dot(b2, b1)*b1
    x = np.dot(v, w)
    y = np.dot(np.cross(b1, v), w)
    return np.degrees(np.arctan2(y, x))


def angle(p) -> float:    
    '''
    Evaluate the angle between 3 atoms

    param: p: 3 positional arraies
    return: float
    '''

    a = p[0]
    b = p[1]
    c = p[2]
    ab = np.linalg.norm(a-b)
    ac = np.linalg.norm(a-c)
    bc = np.linalg.norm(b-c)
    return np.cosh((ac**2+bc**2-ab**2)/(2*ab*bc))

def distance(p) -> float:
    '''
    Evaluate the distance between 2 atoms

    param: p: 2 positional arraies
    return: float
    '''

    a = p[0]
    b = p[1]    
    return np.linalg.norm(a-b)



def sign(indexes, geometry):
    atoms = get_position(geometry, indexes)
    dh = dihedral(atoms)
    print(np.sign(dh))
    return np.sign(dh)