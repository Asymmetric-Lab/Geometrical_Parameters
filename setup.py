"""
Geometrical_Parameters
Geometrical parameters from xyz files. 

To know how to use it, visit our github reopository: https://github.com/Asymmetric-Lab/Geometrical_Parameters

"""

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
        version="1.0.0a",
        url="https://github.com/Asymmetric-Lab/Geometrical_Parameters",
        author="Asymmetric Lab development team",
        author_email="andrea.pellegrini15@unibo.it",
        maintainer="Asymmetric Lab team",
        maintainer_email="andrea.pellegrini15@unibo.it",
        license="MIT License",
        description=doclines,
        # long_description='\n'.join(doclines),
        classifiers=classifiers.split("\n"),
        platforms=["Any."],
        packages=setuptools.find_packages(exclude=['*test*']),
        entry_points={
            'console_scripts': [
                'measure=geom_parameters.measures:ruler',
                'mirror=geom_parameters.mirror:mirror',
                'splitter=geom_parameters.split:splitter',
                'sort_atropo=geom_parameters.sort_atropo:sorter',
            ]
        },
        install_requires=[
            "numpy",
        ],
    )

if __name__ == '__main__':
    setup_()