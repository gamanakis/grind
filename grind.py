#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:26:46 2018

    This program converts exported table data from FlowJo to a format 
    suitable for use with SPICE (niaid.github.io/spice)
    Copyright (C) 2018 Georgios Amanakis (gamanakis@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
print("grind.py  Copyright (C) 2018 Georgios Amanakis (gamanakis@gmail.com)")
print("This program comes with ABSOLUTELY NO WARRANTY;")
print("This is free software, licensed under GPLv3, and you are") 
print("welcome to redistribute it under certain conditions; see LICENSE.txt\n") 

import pandas as pd
import numpy as np

fra = {}
asd = pd.read_csv('Book1.csv', delimiter=',')
print("The columns' names are:\n")
print('\n'.join(list(asd)), '\n')
stable = list(input("Enter column names to be transported\n e.g. Subject Virus :\n" ).split())
delm = input("\nEnter delimiter in column names e.g. PD-1/TIM-3--> / :\n")
neg = input("\nEnter column where none of the markers is expressed :\n")
a = asd.columns.drop(stable)

for col in a:
    nstable = stable.copy()
    nstable.append(col)
    df = asd.loc[:, nstable[:]]
    nstable = stable.copy()
    nstable.append('Value')
    df.columns = nstable
    df.name = col
    if col == neg:
        fra["".join(col)] = df
        continue
    col = col.split(delm)
    for i in range(len(col)):
        df.insert(loc = len(stable) + 1 + i, column = col[i], value='+')
    fra["".join(col)] = df

# Concatenate all dataframes in fra dictionary
df=fra[list(fra.keys())[0]]
for i in range(1, len(list(fra.keys()))):
    df = df.append(fra[list(fra.keys())[i]])    
    
# Replace NaN with '-'
df = df.replace(np.nan, '-')

# Rearrange column names
col = df.columns.tolist()
col.remove('Value')
for i in reversed(range(len(stable))):
    col.remove(stable[i])
    col.insert(0, stable[i])
col.append('Value')
df = df[col]
print("\nThe new columns' names are:\n")
print('\n'.join(col), '\n')

# Write csv
df.to_csv('Book2.csv', index=False)
