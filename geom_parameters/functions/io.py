import os, sys
import shutil


def parse_xyz(file:str) -> list:
    """
    Parse an xyz file with multiple structures

    param: file: filename to be parse

    return: list of xyz-file-like poses
    """

    with open(file) as f:
        fl = f.read()
    fl = fl.splitlines()
    poses = []
    prev_i = 0
    for i in range(int(fl[0].strip())+2, len(fl)+1, int(fl[0].strip())+2):
        if prev_i != 0:
            if fl[prev_i:i]: poses.append('\n'.join(fl[prev_i:i])) 
        else:
            poses.append('\n'.join(fl[:i])) 
        prev_i=i
    return poses



def mkdir(directory, ask=False) -> None:
    """
    Create a directory. If it exists, it will overwrite the directory

    param: directory: name of the directory

    return: None
    """
    if ask: 
        if os.path.exists(directory):
            if input(f'A directory named {directory} already exists. Existing directory will be deleted, wanna procede? [y/n]').lower() not in ['y', 'ye', 'yes']:
                return sys.exit(1)
        
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

    return None