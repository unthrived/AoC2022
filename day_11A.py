import numpy as np

M0 = [83, 88, 96, 79, 86, 88, 70]
M1 = [59, 63, 98, 85, 68, 72]
M2 = [90, 79, 97, 52, 90, 94, 71, 70]
M3 = [97, 55, 62]
M4 = [74, 54, 94, 76]
M5 = [58]
M6 = [66, 63]
M7 = [56, 56, 90, 96, 68]

M = [0,0,0,0,0,0,0,0]


def m0(item):
    
    op = int( (item*5))
    if not op%11: 
        M2.append(op)
    else: 
        M3.append(op)
    M0.pop(0)


def m1(item): 
    op = int( (item*11))
    if not op % 5: 
        M4.append(op)
    else: 
        M0.append(op)
    M1.pop(0)

def m2(item): 
    op = int( (item +2))
    if not op % 19: 
        M5.append(op)
    else: 
        M6.append(op)
    M2.pop(0)

def m3(item): 
    op = int( (item +5))
    if not op % 13: 
        M2.append(op)
    else: 
        M6.append(op)
    M3.pop(0)

def m4(item): 
    op = int( (item*item))
    if not op % 7: 
        M0.append(op)
    else: 
        M3.append(op)
    M4.pop(0)

def m5(item): 
    op = int( (item +4))
    if not op % 17: 
        M7.append(op)
    else: 
        M1.append(op)
    M5.pop(0)

def m6(item): 
    op = int( (item +6))
    if not op % 2: 
        M7.append(op)
    else: 
        M5.append(op)
    M6.pop(0)

def m7(item): 
    op = int( (item +7))
    if not op % 3: 
        M4.append(op)
    else: 
        M1.append(op)
    M7.pop(0)

print(M0, M1, M2, M3, M4, M5, M6, M7)
for j in range(0,20):
    for i in range(len(M0)):
        M[0]+=1
        m0(M0[0])
    for i in range(len(M1)):
        M[1]+=1
        m1(M1[0])
    for i in range(len(M2)):
        M[2]+=1
        m2(M2[0])
    for i in range(len(M3)):
        M[3]+=1
        m3(M3[0])
    for i in range(len(M4)):
        M[4]+=1
        m4(M4[0])
    for i in range(len(M5)):
        M[5]+=1
        m5(M5[0])
    for i in range(len(M6)):
        M[6]+=1
        m6(M6[0])
    for i in range(len(M7)):
        M[7]+=1
        m7(M7[0])
    print(j, M0, M1, M2, M3, M4, M5, M6, M7 ,'\n')
print(M)
print(232*276)