# developer of this code is sandyboyraper plzz dont delete this comment 


import numpy as np

dataX = np.array([[0,0,0],[0,0,1],[1,1,1],[1,1,0]])


XOR = np.array([0,1,1,0])
OR = np.array([0,1,1,1])
AND = np.array([0,0,1,0])

s = str(input())

if s == "XOR":
    dataY = XOR
elif s == "OR":
    dataY = OR
else:
    dataY = AND

Ylen = len(dataY)

px00 = 0.0
px01 = 0.0

py00 = 0.0
py01 = 0.0

pz00 = 0.0
pz01 = 0.0

px10 = 0.0
px11 = 0.0

py10 = 0.0
py11 = 0.0

pz10 = 0.0
pz11 = 0.0

count0 = 0.0

count1 = 0.0

for i in range(Ylen):
    if dataY[i] == 0:
	if dataX[i][0] == 0:
	    px00 = px00+1
	if dataX[i][0] == 1:
	    px01 = px01 + 1
	if dataX[i][1] == 0:
	    py00 = py00 + 1
	if dataX[i][1] == 1:
	    py01 = py01 + 1
	if dataX[i][2] == 0:
	    pz00 = pz00 + 1
	if dataX[i][2] == 1:
	    pz01 = pz01+1
	count0 = count0 + 1
    if dataY[i] == 1:
	if dataX[i][0] == 0:
	    px10 = px10 + 1
	if dataX[i][0] == 1:
	    px11 = px11 + 1
	if dataX[i][1] == 0:
	    py10 = py10 + 1
	if dataX[i][1] == 1:
	    py11 = py11 + 1
	if dataX[i][2] == 0:
	    pz10 = pz10 + 1
	if dataX[i][2] == 1:
	    pz11 = pz11 + 1
	count1 = count1 + 1




px00 = px00 / count0
px01 = px01 / count0
py00 = py00 / count0
py01 = py01 / count0
pz00 = pz00 / count0
pz01 = pz01 / count0



px10 = px10 / count1
px11 = px11 / count1
py10 = py10 / count1
py11 = py11 / count1
pz10 = pz10 / count1
pz11 = pz11 / count1


count0 = count0/4
count1 = count1/4


while 1:


    x = int(input())
    y = int(input())
    z = int(input())

    for0x = 0.0
    for0y = 0.0
    for0z = 0.0
    for1x = 0.0
    for1y = 0.0
    for1z = 0.0



    if x == 0:
        for0x = px00
        for1x = px10
    else:
        for0x = px01
        for1x = px11

    if y == 0:
        for0y = py00
        for1y = py10
    else:
        for0y = py01
        for1y = py11

    if z == 0:
        for0z = pz00
        for1z = pz10
    else:
        for0z = pz01
        for1z = pz11


#print(str(for0x))
#print(str(for1x))

    for0 = for0x*for0y*for0z*count0
    for1 = for1x*for1y*for1z*count1

    print("probability for being 0 ===>>>"+str(for0))

    print("probability for being 1 ===>>>"+str(for1))

    if(for0>for1):
        print(str(0))
    else:
        print(str(1))



















	
        
