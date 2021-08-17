import sys
import os
from sys import stdin

def initialise(MEM):
    i = 0
    for line in stdin:
        if line == '':
            break
        else:
            MEM[i] = line
            i+=1

def getInstruction(PC, MEM):
    pc = "0b" + PC
    pc = int(pc)
    return MEM[pc]

def main():
    MEM = ["0000000000000000"]*256