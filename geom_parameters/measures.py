import argparse
from .func import *

func = {
    2: distance,
    3: angle,
    4: dihedral,
}


def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', nargs='+')
    parser.add_argument('-idx', '--indexes', help='Define indexes for the measure. One measure at a time', nargs='+', action=required_length(2, 4))

    return parser.parse_args()


def ruler():
    args = parse()
    ruler = func[len(args.indexes)]

    for file in args.file:
        confs = parse_xyz(file)
        for idx, i in enumerate(confs):
            p = get_position(i, args.indexes, read=False, geom=True)
            print(f'{file} - {idx} - {ruler(p):.2f}')


if __name__ == '__main__':

    ruler()