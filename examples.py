#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Demonstrations and examples of pyqtmpl usage
"""

# Basic imports
from __future__ import print_function, division
import sys
import warnings

# Calculation imports
import numpy as np

# GUI imports
from PyQt4 import QtGui

# pyqtmpl
from pyplot import subplots


def demo_plot():
    x = np.linspace(0, 10, 151)
    y1 = x**2 + 1
    y2 = x*10 - 0.1 * x**3 + 50
    y3 = 85 - y1
    fig, axs = subplots(3, 2, sharex='col', sharey='row', gridspec_kw={'left': 0.25, 'right': 0.95}, dpi=300)
    axs[-1, 0].set_xlabel('x')
    axs[-1, 1].set_xlabel('X')
    axs[0, 0].set_ylabel('y')
    axs[1, 0].set_ylabel('y')
    axs[2, 0].set_ylabel('y')

    axs[0, 0].plot(x, y1)
    axs[0, 1].plot(x, y2)
    axs[0, 1].plot(x, y3)

    axs[1, 0].plot(x, y1, color='r')
    axs[1, 0].plot(x, y2, color='k')
    axs[1, 1].plot(x, y2, linestyle='--', color='g')
    axs[1, 1].plot(x, y3, linestyle='-.', color='b')

    axs[2, 0].plot(x, y1, color='m', marker='o')
    axs[2, 1].plot(x, y2, linestyle=' ', color='k', marker='+')
    axs[2, 1].plot(x, y3, linestyle=' ', color='k', marker='x')

    axs[1, 0].axvline(np.mean(x), linestyle=':', color='k')
    axs[1, 0].axhline(np.mean(y1), linestyle='-', color='k')

    return fig, axs


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    demo_plot()
    # Start Qt event loop unless running in interactive mode or using pyside.
    if __name__ == '__main__':
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            app.exec_()
