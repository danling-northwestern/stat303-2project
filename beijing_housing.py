#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:12:44 2023

@author: danling zhou
"""

import pandas as pd

beijing_house = pd.read_csv('beijing_house.csv',encoding='utf-16',on_bad_lines='skip')