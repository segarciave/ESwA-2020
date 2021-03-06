# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:59:30 2018

@author: Sergio GARCIA-VEGA
sergio.garcia-vega@manchester.ac.uk
The University of Manchester, Manchester, UK
BigDataFinance, Work Package 1, Research Project 1
Id: OPF.py
"""

import numpy as np


def gaus_kernel(u,dicti,kpar):
    """
    Computes the Gaussian kernel for two data sets.
    
    FORMAT:
        kernel = gaus_kernel(u,dicti,kpar)
        
        INPUTS:
        ______________________________________________________________________
        |   NOTATION    |         DESCRIPTION         |         TYPE          |
        |---------------|-----------------------------|-----------------------|
        |   u           | Input vector                | Row vector (numpy)    |
        |---------------|-----------------------------|-----------------------|
        |   dicti       | Dictionary                  | Matrix (numpy)        |
        |---------------|-----------------------------|-----------------------|
        |   kpar        | Kernel bandwidth            | Positive real number  |
        ----------------|-----------------------------|------------------------
        
        OUTPUTS:
        ______________________________________________________________________
        |   NOTATION    |         DESCRIPTION         |         TYPE          |
        |---------------|-----------------------------|-----------------------|
        |   kernel      | kernel                      | Row vector (numpy)    |
        -----------------------------------------------------------------------
        __________________________________________________
        Outside functions called (user-defined functions):
        - None
        ______________________________________________________________________
    """
    num    = np.linalg.norm(u-dicti, axis=1)**2
    den    = 2*kpar**2
    kernel = np.exp(-(num)/(den))[np.newaxis,:]
    return kernel