import numpy as np

M0 = [79, 98]
M1 = [54, 65, 75, 74]
M2 = [79, 60, 97]
M3 = [74]

def m0(item): 
    op = int((item * 19)/3)
    if not op % 23: 
        M2.append(op)
        M0.pop(0)
    else: 
        M3.append(op)
        M0.pop(0)

def m1(item): 
    op = int( (item +6)/3)
    if not op % 19: 
        M2.append(op)
    else: 
        M0.append(op)
    M1.pop(0)

def m2(item): 
    op = int((item * item )/3)
    if not op % 13: 
        M1.append(op)
        M2.pop(0)
    else: 
        M3.append(op)
        M2.pop(0)

def m3(item): 
    op = int((item+3 )/3)
    if not op % 17: 
        M0.append(op)
        M3.pop(0)
    else: 
        M1.append(op)
        M3.pop(0)


print(M0, M1, M2, M3)
for i in range(len(M0)):
    m0(M0[0])
for i in range(len(M1)):
    m1(M1[0])
for i in range(len(M2)):
    m2(M2[0])
for i in range(len(M3)):
    m3(M3[0])
print(M0, M1, M2, M3)
