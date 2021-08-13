import sys
import os


Lines = []
output = []
from sys import stdin



def instruction_call(arr):
	dic={
	'add': '00000' , 
	'sub': '00001', 
	'mov':'00010',
	'mov1': '00011',
	'ld':'00100',
	'st':'00101', 
	'mul':'00110',
	'div':'00111',
	'rs':'01000', 
	'ls':'01001',
	'xor':'01010',
	'or':'01011',
	'and':'01100',
	'not':'01101',
	'cmp':'01110',
	'jmp':'01111',
	'jlt':'10000',
	'jgt':'10001',
	'je':'10010',
	'hlt':'10011'}
	if(arr[0]=="add" or arr[0]=="sub" or arr[0]=="mul" or arr[0]=="xor" or arr[0]=="or" or arr[0]=="and"):
		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c = encodeA(arr[2])
		d = encodeA(arr[3])
		if(b=='-1' or c=='-1' or d=='-1'):
			#clear()
			print("Wrong syntax in type A")
			exit()
		else:
			out=(a+"00"+b+c+d)
			output.append(out)
	
	elif(arr[0]=="ls" or arr[0]=="rs" or (arr[0]=="mov" and arr[1][0]=='R' and  arr[2][0]=="$")):
		#move imm in flags??
		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c=arr[2]
		d = c[1:]
		if(d.isnumeric() == True):
			d = int(d)
		else:
			d = -1
		p=bnr(c)
		if (b == '-1' or c == '-1' or d == '-1'):
			#clear()
			print("Wrong syntax in type b")
			exit()
		if(d<0 or d>255):
			#clear()
			print("Value out of range")
			exit()
		else:
			out=(a+b+p)
			output.append(out)

	elif(arr[0] == "mov" and arr[1][0]=="R" and arr[2][0]=="R"):
		#print('here')
		#instead check if arr[1][0] in dic1 of labels 
		#move r1 in flags?
		a = dic.get("mov1")
		b = encodeC(arr[1])
		c = encodeC(arr[2])

		if(b=='-1' or c=='-1'):
			#clear()
			print("Wrong syntax in movr")
			exit() 
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif(arr[0] == "mov" and arr[1][0]=="R" and arr[2]=="FLAGS"):
		a = dic.get("mov1")
		b = encodeC(arr[1])
		c = encodeC(arr[2])
		if(b=='-1' or c=='-1'):
			#clear()
			print("Wrong syntax in movr")
			exit() 
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif (arr[0] == "div" or arr[0] == "not" or arr[0] == "cmp"):
		

		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c = encodeA(arr[2])
		if(a=='-1' or b=='-1' or c=='-1'):
			#clear()
			print("Wrong syntax in compare")
			exit()
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif (arr[0] == "ld" or arr[0] == "st"):
		a = dic.get(arr[0])
		b = encodeA(arr[1])
	#c=variable value
		c = variable_value(arr[2])
		if(a==-1 or b==-1):
			#clear()
			print("Wrong syntax in ld or st")
			exit()
		out=(a+b+c)
		output.append(out)

	elif (arr[0] == "je" or arr[0] == "jlt" or arr[0]=="jmp" or arr[0]=="jgt"):
		
		a=dic.get(arr[0])
		b=dictLabel.get(arr[1])
		b3=(bin(b))[2:]
		
		b4=b3.zfill(8)
		
		
		
		
		##b2=bin(int(str1[1:]))[2:]
		#txt1 = b2.zfill(8)
					
		if(b==-1):
			#clear()
			print("Wrong syntax in E")
			exit()
		else:
			out=(a+"000"+b4)
			output.append(out)


	elif(arr[0]=="hlt"):
		a = dic.get(arr[0])
		out=(a + "00000000000")
		output.append(out)

	elif (arr[0][-1]==':' ):
		arr.pop(0)
		if arr != []:
			instruction_call(arr)
		else:
			return

	

	else:
		#clear()
		print("Wrong syntax no  type found")
		exit()



def bnr(a):
	if a[0] == '$':
		b = a[1:]
		if b.isnumeric() == True:
			c =  bin(int(a[1:]))[2:]
			txt = c.zfill(8)
			return txt
	else: 
		return -1


def variable_value(x):
	a=int(indexHalt)
	b=listVar.index(x)
	k=a+b+1
	ans=bin(k)[2:]
	ans1=(str(ans)).zfill(8)
	return ans1

arr=[]
def encode(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	elif a == 'FLAGS':
		return '111'
	elif a[0] == '$':
		b = a[1:]
		if b.isnumeric() == True:
			return bin(int(a[1:]))[2:]  # else error
		else:
			return '-1'
			
	else:
		return '-1'

def encodeC(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	elif a == 'FLAGS':
		return '111'
	else:
		return -1

def encodeA(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	else:
		return -1

for line in stdin:
	line = line.strip()
	if line == '':
		break
	Lines.append(line)



#print(Lines)

count = 0
listVar = []
dictLabel = {}
countVar=0
indexHalt = 0
flag = True
for line in Lines:
	line = line.strip()
	count+=1
	if line[0:3] == "var" and len(line) > 3 and listVar.count(line[4:]) == 0:
		listVar.append(line[4:])
		countVar += 1
		if countVar<count:
			flag = False
			break
	elif line[0:3] == "var" and listVar.count(line[4:]) != 0:
		flag = False

count = 0
arr1= Lines[-1]
arr1=arr1.split()
flag1=False
if(arr1[0][-1]==':' and arr1[-1]=='hlt' and arr1[1]=='hlt'):
	flag1 =True
	flag =True
	str1=''
	for e in Lines[-1]:
		str1+=e
	indexHalt = Lines.index(str1) -countVar
	
#print('hello') ###########################################################3
if flag == False:
	#Error message
	print("ERROR:flag false ")
	exit()

if Lines.count("hlt") > 1 or Lines.count("hlt") == 0 and flag1==False:
	#print('0 or >1') ###########################################################
	flag = False

	exit()

if(Lines.count("hlt") != 0):
	indexHalt = Lines.index("hlt") -countVar 
if len(Lines) - countVar > indexHalt + 1:
	#print(countVar)
	#print(indexHalt)
	flag = False
	exit()

elif flag == True:
	for line in Lines:
		line = line.strip()
		if line != "hlt" and line[0:3] != "var":
			if line.count(":") == 1:
			
				t1 = line.index(":")
				dictLabel[line[:t1]] = count 
				if line.index(":") + 1 == len(line):
					count -= 1
			if line.count(":") > 1:
				flag = False
			count += 1

if flag == False:
	#Error message
	print("ERROR:flag false ")
	exit()

elif flag == True:

	for line in Lines:
		if line[0:3] != "var":
			line = line.strip()
			arr = line.split()
			instruction_call(arr)
	for i in output:
		print(i)
