import argparse
import os
from .func import *



def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='Add an xyz file to parse', nargs='+')
    parser.add_argument('-d', '--directory', help='Change the name of the directory. If more file selected it creates more directory, one for each file', default='structures')

    return parser.parse_args()

def split(fname:str, len_files:int, d:str, idx:int) -> None:

    directory = d (str(idx) if len_files>1 else '')
    mkdir(directory, True)

    poses = parse_xyz(fname)

    flag = 'CONF' in poses[0].splitlines()[1]

    for idx, pose in enumerate(poses): 
        fn = pose.splitlines()[1].split()[-1].strip('!')+'.xyz' if flag else 'CONF'+str(idx)+'.xyz'

        with open(os.path.join(directory, fn), 'w') as f:
            f.write(pose)

    return None


def splitter():
    args = parse()
    for idx, fname in enumerate(args.file):
        split(fname, len(args.file), args.directory, idx)

        

