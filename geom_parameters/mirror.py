import numpy as np
import os
import argparse
from .func import *


def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', nargs='+')
    return parser.parse_args()

def get_geometry(points):
    geom = np.array([i.split()[1:] for i in points], dtype=np.float64)
    return geom*[-1, 1, 1]


def write_xyz(inp, idx, out, atoms, en_geom):
    o = os.path.join(os.getcwd(), out)
    with open(o, 'a') as f:
        f.write(str(len(en_geom))+'\n')
        f.write('Enantiomer of {0}-{1}\n'.format(inp, idx))
        for a, i in zip(atoms, en_geom):
            f.write('%s \t %.5f \t %.5f \t %.5f \n' % (a, *i))


def mirror():
    args = parse()
    for fname in args.file:
        gs = parse_xyz(fname)
        for idx, g in enumerate(gs):
            g = g.splitlines()
            atoms = [i.split()[0] for i in g[2:] if i]
            en = get_geometry(g[2:])
            fn = os.path.split(fname)[1].split('.')[0]
            write_xyz(fn, idx, f'en_{fn}_{idx}.xyz', atoms, en)




if __name__ == '__main__':
    mirror()