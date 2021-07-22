# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:31:51 2021

@author: ABC
"""

n = int(input())
x = list(map(int,input().split()))
cnt = 0
count = 0
for i  in x:
    if i%2==0:
        cnt+=1
    count+=1

if cnt>(count/2):
    print("READY FOR BATTLE")    
else:
    print("NOT READY")    