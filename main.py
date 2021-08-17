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

def flagReset(RF):
    RF[7] = "0000000000000000"

def main():
    MEM = ["0000000000000000"]*256
    RF = ["0000000000000000"]*8
    PC = 0
    initialise(MEM)
    halted = False

def execute(Instruction, RF, MEM, PC):

    #Type A
    if(Instruction[0:5]=="00000" or Instruction[0:5]=="00001" or Instruction[0:5]=="000110" or Instruction[0:5]=="001010" or Instruction[0:5]== "001011" or Instruction[0:5]=="01100"):
        flagReset(RF)
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

    #Type B
    if (Instruction[0:5] == "00010" or Instruction[0:5] == "01000" or Instruction[0:5] == "01001"):
        flagReset(RF)
        a = int(Instruction[5:8], 2)
        b = int(Instruction[8:], 2)
        if (Instruction[0:5] == "00010"):
            val = Instruction[8:].zfill(16)
            RF[a] = val
            return False, PC + 1

        elif(Instruction[0:5] == "01000"):
            val = RF[a]
            intVal = int(val, 2)
            finVal = intVal >> b
            finVal = (bin(finVal)[2:]).zfill(16)
            RF[a] = finVal
            return False, PC + 1

        elif(Instruction[0:5] == "01001"):
            val = RF[a]
            intVal = int(val, 2)
            finVal = intVal << b
            finVal = (bin(finVal)[2:]).zfill(16)
            RF[a] = finVal
            return False, PC + 1


    #Type C
    if(Instruction[0:5] == "00011" or Instruction[0:5] == "00111" or Instruction[0:5] == "01101" or Instruction[0:5] == "01110"):
        
        a = int(Instruction[10:13], 2)
        b = int(Instruction[13:16], 2)
        if(Instruction[0:5] == "00011"):
            val = RF[b]
            RF[a] = val
            flagReset(RF)
            return False, PC + 1

        if(Instruction[0:5] == "00111"):
            flagReset(RF)
            op1 = int(RF[a], 2)
            op2 = int(RF[b], 2)
            q = int(op1/op2)
            r = int(op1%op2)
            RF[0] = bin(q)[2:].zfill(16)
            RF[1] = bin(r)[2:].zfill(16)
            #overflow
            return False, PC + 1

        if(Instruction[0:5] == "01101"):
            flagReset(RF)
            op2 = RF[b]
            inverse = ""
            for i in op2:
                if i == "0":
                    inverse += "1"
                else:
                    inverse += "0"
            RF[a] = inverse
            return False, PC + 1

        if(Instruction[0:5] == "01110"):
            flagReset(RF)
            op1 = int(RF[a], 2)
            op2 = int(RF[b], 2)
            if(op1<op2):
                RF[7] = "0000000000000100"
            elif(op1>op2):
                RF[7] = "0000000000000010"
            elif(op1 == op2):
                RF[7] = "0000000000000001"
            return False, PC + 1


    #Type D
    if (Instruction[0:5]=="00100" or Instruction[0:5]=="00101" ):
        flagReset(RF)     
        a=int(Instruction[5:8] ,2)
        b=int(Instruction[8:], 2)
        if(Instruction[0:5]=="00100"): 
            RF[a]= MEM[b]
            return False, PC + 1

        if(Instruction[0:5]=="00101"):
            MEM[b]=RF[a]
            return False, PC + 1




