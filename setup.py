# -*- coding: utf-8 -*-

"""
Set-up
-----------------
"""

from distutils.core import setup


setup(
    name='mentoria-ayv',
    version='0.1',
    description='Analisis y visualizacion de datos',
    install_requires=[
        'requests'
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'jupyterlab',
        'scipy',
    ]
)
