#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:04:46 2018

@author: jimhs
"""

from collections import deque

# cook 4.1
# basic use: StopIteration | None
#with open('/etc/passwd') as f:
##    try:
##        while True:
##            line = next(f)
##            print(line, end='')
##    except StopIteration:
##        pass
#    while True:
#        line = next(f, None)
#        if line is None:
#            break
#        print(line, end='')

# cook 4.6
class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
            
    def clear(self):
        self.history.clear()

with open('/etc/passwd') as f:
    lines = LineHistory(f)
    for line in lines:
        if 'nologin' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')