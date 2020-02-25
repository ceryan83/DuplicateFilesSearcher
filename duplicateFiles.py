# -*- coding: utf-8 -*-
"""
Duplicate Music Files Search
Created on Fri Nov 15 15:13:19 2019

@author: cerya

This program searches a directory and all of its subdirectories for .mp3 files.
After finding all .mp3 files within the directory, it performs a md5 checksum
to determine if there are any duplicates.
"""
import os


def search_for_type(parent, suffix, t = list()):
    """
    Searches a directory and all of its subdirectories for files of a given
    type. Outputs a list of relevant files.
    """    
    for name in os.listdir(parent):
        path = os.path.join(parent, name)
        if os.path.isfile(path):
            if suffix in path:
                t.append(path)
        else:
            search_for_type(path, suffix, t)        
    return t

def find_all_duplicates(t):
    """
    Takes a list of filenames as input and outputs all duplicate pairs of files
    after performing a checksum to test for duplicates.
    """    
    sums = list()
    for item in t:
        #perform checksum and store it in sums
    for i in range(len(sums)-1):
        for j in range(i+1, len(sums)):
            if sums[i] == sums[j]:
                print('The files {0} and {1} are duplicates.'.format(t[i],t[j]))

cwd = os.getcwd() 
t = search_for_type('C:\\Users\\cerya\\Dropbox\\ComputerScience', '.txt')
