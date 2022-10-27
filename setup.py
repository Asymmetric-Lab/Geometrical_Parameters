import setuptools
# Chosen from http://www.python.org/pypi?:action=list_classifiers
classifiers = """Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Topic :: Scientific/Engineering :: Chemistry
Topic :: Software Development :: Libraries :: Python Modules"""

def setup_():
    doclines = __doc__.split("\n")
    setuptools.setup(
        name="Geometrical Parameter",
        version="1.0.0",
        url="",
        author="Asymmetric Lab development team",
        author_email="andrea.pellegrini15@unibo.it",
        maintainer="Asymmetric Lab team",
        maintainer_email="andrea.pellegrini15@unibo.it",
        license="BSD 3-Clause License",
        description=doclines[0],
        long_description="\n".join(doclines[2:]),
        classifiers=classifiers.split("\n"),
        platforms=["Any."],
        packages=setuptools.find_packages(exclude=['*test*']),
        entry_points={
            'console_scripts': [
                'measure=geom_parameters.scripts.measueres:ruler',
                'mirror=geom_parameters.scripts.mirror:mirror',
                'split=geom_parameters.scripts.split:splitter',
                'sort_atropo=geom_parameters.scripts.sort_atropo:sorter',
            ]
        },
        install_requires=[
            "numpy",
        ],
    )

if __name__ == '__main__':
    setup_()