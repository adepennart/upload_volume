#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: upload_volume.py
Date: October 9th, 2023
Author: Auguste de Pennart
Description:
    uploads volumes onto Catmaid

List of functions:
    No user defined functions are used in the program.

List of "non standard modules"
    No user defined modules are used in the program.

Procedure:
    1. Takes project id and volume file of interest
    2. logs into Catmaid account
    3. uploads volume in Catmaid project

Usage:
    python upload_volume.py [-h] [-v] -p PROJECT_ID -i INPUTFILE [-n NAME]
                        [-r RESIZE] [-s]

known error:
    1. only takes one input file at a time, inputting a folder with input files would be good 
    2. resize option changes all 3 dimensions proportionally (x,y,z), no option to change one dimension
 """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #fix it so it displays name of file here
    print('using upload_pymaid.py as main script')

# import modules
# ----------------------------------------------------------------------------------------
# import re  # module for using regex
import argparse #module for terminal use
import pymaid
# import pandas
import matplotlib.pyplot as plt
import navis
import numpy
# import matplotlib.colors
# import json
# import sys
# print(sys.path)

# import os
# import sys
# import inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

#from  plot_functions import *

# variables
# --------------------------------------------------------------------------------------
inputfile="example.stl"
project_id=100
name="example"
resize=None
show=None

#argparse
# ----------------------------------------------------------------------------------------
#program description
usage='uploads volumes onto Catmaid'
parser=argparse.ArgumentParser(description=usage)#create an argument parser
reqgroup= parser.add_argument_group(title='required arguments')

#creates the argument for program version
parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s 1.0')
#creates the argument where project_id will be inputted
reqgroup.add_argument('-p', '--project_id',
                    metavar='PROJECT_ID',
                    dest='project_id',
                    required=True,
                    help='user-specified project id (ie. lamarcki_OV)')
#creates the argument where the json file will be inputted
reqgroup.add_argument('-i', '--inputfile',
                    metavar='INPUTFILE',
                    dest='inputfile',
                    required=True,
                    nargs=1,
                    help='user-specified STL ascii (.stl) file')
#creates the argument where the neuron(s) be inputted
parser.add_argument('-n', '--name_of_volume',
                    metavar='NAME',
                    dest='name',
                    nargs=1,
                    help='user-specified Neuron(s) of interest. REGEX accepted.')
#creates the argument where the plot perspective will be inputted
parser.add_argument('-r', '--resize',
                    metavar='RESIZE',
                    dest='resize',
                    nargs=1,
                    help='User-specified resize factor (i.e., input 10, 10 times larger)')
#creates the argument whether to show or not the plot
parser.add_argument('-s', '--show',
                    dest='show',
                    action='store_true',
                    default=None,
                    help='option to show plot')
args=parser.parse_args()#parses command line


# main code
# --------------------------------------------------------------------------------------
rm = pymaid.connect_catmaid(project_id=args.project_id)#open Catmaid to project id
a_volume=navis.Volume.from_file(args.inputfile)
print("coordinates of boundingbox are ", a_volume.bbox)
if args.resize:
    a_volume=a_volume.resize(args.resize, method='origin', inplace=False)
if args.show:
    fig, ax = navis.plot2d([a_volume]) #setup figure
    plt.show()
pymaid.upload_volume(a_volume, name=args.name[0], comments=None, remote_instance=None)


