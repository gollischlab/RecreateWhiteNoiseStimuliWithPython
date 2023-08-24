from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name='retinawhitenoise._rng',
            sources=['rng/rng.pyx'],
            include_dirs=['rng'],
            language="c++",
        ),
    ]
)
