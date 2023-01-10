# Geometrical Parameters


Retrieve geometrical parameters from _xyz_ files. 

This package is formed by 4 scripts: 
- `measure`: measure a distance, an angle or a dihedral of a geometry.
- `mirror`: obtain the enantiomeric image of a structure.
- `sort_atropo`: sort an ensemble based on a dihedral value.
- `splitter`: divide an ensemble into single xyz files.

---

<br>

## To install 

### _Using pip_

```bash 
pip install Geometrical_Parameter
```

### _Form code_

1. Clone this repository
1. `cd geometrical_parameters`
1. `pip install .`
1. When pulling the repository, hit the command `pip install --upgrade .`

---
## Usages

### Measure package
```bash
usage: measure [-h] [-idx INDEXES [INDEXES ...]] file [file ...]

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -idx INDEXES [INDEXES ...], --indexes INDEXES [INDEXES ...]
                        Define indexes for the measure. One measure at a time
```

### Mirror package
```bash
usage: mirror [-h] file [file ...]

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
```

### Sort_diastero package
```bash
usage: sort_atropo [-h] -i INDEX [INDEX ...] file [file ...]

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -i INDEX [INDEX ...], --index INDEX [INDEX ...]
                        Define the index (starting at 1) of the atoms
```

### Splitter package
```bash
usage: splitter [-h] [-d DIRECTORY] file [file ...]

positional arguments:
  file                  Add an xyz file to parse

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Change the name of the directory. If more file selected it creates more directory, one for each file
```