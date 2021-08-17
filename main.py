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
    return MEM[PC]

def main():
    MEM = ["0000000000000000"]*256
    RF = ["0000000000000000"]*8
    PC = 0
    initialise(MEM)
    halted = False

def execute(Instruction, RF):
     def execute(Instruction, RF):
    if(Instruction[0:5]=="00000" and Instruction[0:5]=="00001" and Instruction[0:5]=="000110" and Instruction[0:5]=="001010" and Instruction[0:5]== "001011" and Instruction[0:5]=="01100"):
        a=int(Instruction[7:10] , 2) 
        b =int(Instruction[10:13] , 2) 
        c= int(Instruction[13:16], 2)
        if(Instruction[0:5]=="00000"):
            d= int(int(RF[b]),2) + int(int(RF[c]),2)
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
        #overflow

        if(Instruction[0:5]=="00001"):
            d= int(int(RF[b]),2) - int(int(RF[c]),2)
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val              #-ve subtraction

        if(Instruction[0:5]=="000110"):
            d= int(int(RF[b]),2) * int(int(RF[c]),2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val 
        if(Instruction[0:5]=="001010"):    # xor
            d= int(int(RF[b]),2) ^ int(int(RF[c]),2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val

        if(Instruction[0:5]=="001100"):   # and 
            d= int(int(RF[b]),2) & int(int(RF[c]),2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
        
        if(Instruction[0:5]=="001011"): # or
            d= int(int(RF[b]),2) | int(int(RF[c]),2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
            
    if (Instruction[0:5] == "00010" or Instruction[0:5] == "01000" or Instruction[0:5] == "01001"):
        a = int(Instruction[5:8], 2)
        b = int(Instruction[8:], 2)
        if (Instruction[0:5] == "00010"):
            val = Instruction[8:].zfill(16)
            RF[a] = val
        elif(Instruction[0:5] == "01000"):
            val = RF[a]
            intVal = int(val, 2)
            finVal = intVal >> b
            finVal = (bin(finVal)[2:]).zfill(16)
            RF[a] = finVal
        elif(Instruction[0:5] == "01001"):
            val = RF[a]
            intVal = int(val, 2)
            finVal = intVal << b
            finVal = (bin(finVal)[2:]).zfill(16)
            RF[a] = finVal
    
   
      


