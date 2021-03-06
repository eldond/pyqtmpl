#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# Basic imports
from __future__ import print_function, division
import sys
import os

# GUI imports
from pyqtgraph import QtGui

# Plotting imports
import pyqtgraph as pg
from matplotlib import rcParams

# pgmpl imports
from pgmpl.info import *  # Defines __version__, etc.
from pgmpl.util import printd
from pgmpl.translate import color_translator

__all__ = ['figure', 'axes', 'pyplot', 'translate', 'text', 'util']

# Handle debugging
if os.environ.get('PGMPL_DEBUG', None) is None:
    os.environ['PGMPL_DEBUG'] = "0"

# Setup style, etc.
pg.setConfigOption('background', color_translator(**{'color': rcParams['axes.facecolor']}))
pg.setConfigOption('foreground', color_translator(**{'color': rcParams['axes.edgecolor']}))

# Check for an existing QApp and make one if none found so that windows can be opened
app = QtGui.QApplication.instance()
if app is None:
    printd('No pre-existing QApplication found. Creating one...')
    app = QtGui.QApplication(sys.argv)
else:
    printd('Using pre-existing QApplication.')
