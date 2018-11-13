#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:55:57 2018

@author: Javier
"""

#%%

import utils.functions
import data.triangles

def calculate_triangles():
    for i in data.triangles.triangle_definitions:
        print(utils.functions.area_triangle(i["base"],i["height"]))
    
calculate_triangles()