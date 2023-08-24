# RecreateWhiteNoiseStimuliWithPython
Code for regenerating the random-number-based contrast values applied in experiments with white-noise stimulation in the Gollisch Lab.
Used for both temporal and spatiotemporal stimuli, and for both binary and Gaussian white noise.

The random-number sequences are needed for analyzing the spike responses of recorded cells under white-noise stimulation.

### Installation
The Python package contains Cython code (C++) to be compiled before use.

A full installation of the package is done with
```
pip install https://github.com/gollischlab/RecreateWhiteNoiseStimuliWithPython/archive/main.tar.gz
```

### Usage
The Python package `retinawhitenoise` offers two modules `binarystimulus` and `gaussianstimulus`,
each offering routines to `recreate`, `save` (to disk), and `load` stimulus sequences.

Instructions on how to use them with example code and explanations is included in the jupyter notebook `examples.ipynb`.
