# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:48:59 2021

@author: ABC
"""
'''
count = 0
t = int(input())
for i in range(t):
    t_1,t_2 = input().split()
    for j in range(int(t_1)):
        x = str(input())
        if t_2 == 'INDIAN':
            if x == 'CONTEST_WON 1':
                count+=319
            if x == 'TOP_CONTRIBUTOR':
                count+=300
            if x == 'BUG_FOUND 100':
                count+=100
            if x == 'CONTEST_HOSTED':
                count+=50
    
            
        if t_2 == 'NON_INDIAN':
            if x == 'CONTEST_WON 1':
                count+=319
            if x == 'TOP_CONTRIBUTOR':
                count+=300
            if x == 'BUG_FOUND 100':
                count+=100
            if x == 'CONTEST_HOSTED':
                count+=50
    
    if t_2 == 'INDIAN':
        print(count-(count%200)//200)
    if t_2 == 'NON_INDIAN':    
        print(count-(count%400)//400)
        
'''
for t in range(int(input())):
    l=0
    n,p=input().split()
    n=int(n)
    for j in range(n):
        z=input().split()
        s=z[0]
        if (len(z)!=1):
                x=int(z[1])
        if (s=='CONTEST_WON'):
            if (x<=20):
                l=l+(320-x)
            else:
                l=l+300
        elif (s=='TOP_CONTRIBUTOR'):
            l=l+300
        elif (s=='BUG_FOUND'):
            l=l+x
        else:
            l=l+50
    if (p=='INDIAN'):
        a=(l//200)
    else:
        a=(l//400)
    print(a)        