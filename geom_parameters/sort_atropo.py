import argparse, os
from const_func import mkdir, parse_xyz, sign



def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', nargs='+')
    parser.add_argument('-i', '--index', help='Define the index (starting at 1) of the atoms', nargs='+', required=True)

    return parser.parse_args()

def write_atropo(d:str, poses:list, idxs:list):
    for idx, i in enumerate(idxs): 
        with open(os.path.join(d, f'{str(idx)}.xyz'), 'w') as f:
            f.write(poses[idx])


def sort(fname, index):
    poses = parse_xyz(fname)
    p, n = [], []

    for idx, geom in enumerate(poses):
        if sign(index, geom, geom=True) > 0:
            p.append(idx)
        else:
            n.append(idx)

    mkdir(f'{fname}_pos')
    with open(os.path.join(f'{fname}_pos', f'{fname}_p.xyz'), 'w') as f:
        f.write('\n'.join([poses[i] for i in p]))
    write_atropo(f'{fname}_pos', poses, p)

    mkdir(f'{fname}_neg')
    with open(os.path.join(f'{fname}_neg', f'{fname}_n.xyz'), 'w') as f:
        f.write('\n'.join([poses[i] for i in n]))
    write_atropo(f'{fname}_neg', poses, n)


def sorter():
    args = parse()

    for fname in args.file:
        sort(fname, args.index)
            
        
if __name__ == "__main__":
    sorter()