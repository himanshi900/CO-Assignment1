
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

def printRF(RF):
    s = ""
    for i in range(8):
        s += RF[i] + " "
    return s

def printPC(PC):
    s = bin(PC)[2:].zfill(8)
    return s

def printMEM(MEM):
    for i in range(256):
        print(MEM[i].rstrip())

def execute(Instruction, RF, MEM, PC):

    #Type A
    if(Instruction[0:5]=="00000" or Instruction[0:5]=="00001" or Instruction[0:5]=="000110" or Instruction[0:5]=="001010" or Instruction[0:5]== "001011" or Instruction[0:5]=="01100"):
        flagReset(RF)
        a=int(Instruction[7:10] , 2) 
        b =int(Instruction[10:13] , 2) 
        c= int(Instruction[13:16], 2)
        if(Instruction[0:5]=="00000"):
            d= int(RF[b],2) + int(RF[c],2)
            if(d>65535):
                RF[7] == "0000000000001000"
                s= str(bin(d))[2:]
                l = len(s) - 16
                val = s[l:].zfill(16)
                RF[a] = val
                return False, PC + 1 
            else:
                s= str(bin(d))
                val = s[2:].zfill(16)
                RF[a] = val
                return False, PC + 1
        #overflow

        if(Instruction[0:5]=="00001"):
            d= int(RF[b],2) - int(RF[c],2)      
            if(d<0):
                RF[7]="0000000000001000"
                s= "0000000000000000" 
                RF[a] = s 
                return False, PC + 1
            else:
                s= str(bin(d))         #-ve subtraction
                val = s[2:].zfill(16)
                RF[a] = val
                return False, PC + 1

        if(Instruction[0:5]=="00110"):
            d= int(RF[b],2) * int(RF[c],2) #overflow check
            if(d>65535):
                RF[7] == "0000000000001000"
                s= str(bin(d))[2:]
                l = len(s) - 16
                val = s[l:].zfill(16)
                RF[a] = val
                return False, PC + 1 
            else:
                s= str(bin(d))
                val = s[2:].zfill(16)
                RF[a] = val
                return False, PC + 1 


        if(Instruction[0:5]=="001010"):    # xor
            d= int(RF[b],2) ^ int(RF[c],2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
            return False, PC + 1

        if(Instruction[0:5]=="001100"):   # and 
            d= int(RF[b],2) & int(RF[c],2) #overflow
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
            return False, PC + 1
        
        if(Instruction[0:5]=="001011"): # or
            d= int(RF[b],2) | int(RF[c],2) 
            s= str(bin(d))
            val = s[2:].zfill(16)
            RF[a] = val
            return False, PC + 1

    #Type B
    if (Instruction[0:5] == "00010" or Instruction[0:5] == "01000" or Instruction[0:5] == "01001"):
        flagReset(RF)
        a = int(Instruction[5:8], 2)
        b = int(Instruction[8:], 2)
        if (Instruction[0:5] == "00010"):
            val = bin(b)[2:].zfill(16)
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
            #if(op2==0):
            
            q = int(op1/op2)
            r = int(op1%op2)
            RF[0] = bin(q)[2:].zfill(16)
            RF[1] = bin(r)[2:].zfill(16)
            
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
    #Type E
    if(Instruction[0:5]=="01111" or Instruction[0:5]=="10000" or  Instruction[0:5]=="10001" or Instruction[0:5]=="10010"):
        a = int(Instruction[8:], 2)
        if(Instruction[0:5]=="01111"):
            flagReset(RF)
            return False, a
        
        elif(Instruction[0:5]=="10000"):
            if(RF[7][-3]== "1"):
                flagReset(RF)
                return False, a
            else:
                flagReset(RF)
                return False, PC + 1

    
        elif(Instruction[0:5]=="10001"):
            if(RF[7][-2]=="1"):
                flagReset(RF)
                return False, a
            else:
                flagReset(RF)
                return False, PC + 1


        elif(Instruction[0:5]=="10010"):
            if(RF[7][-1]=="1"):
                flagReset(RF)
                return False, a
            else:
                flagReset(RF)
                return False, PC + 1 
    
    #Type F
    if(Instruction[0:5] == "10011"):
        flagReset(RF)
        return True, PC + 1
        
def main():
    MEM = ["0000000000000000"]*256
    RF = ["0000000000000000"]*8
    PC = 0
    initialise(MEM)
    halted = False
    while(not halted):
        Instruction = getInstruction(PC, MEM) # Get current instruction
        halted, new_PC = execute(Instruction, RF, MEM, PC) # Update RF compute new_PC
        a = printPC(PC)
        b = printRF(RF)
        print(a + " " + b)
        PC = new_PC
    printMEM(MEM)

main()        
            
            

        



    
