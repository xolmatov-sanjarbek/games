# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:04:02 2024

@author: user
"""

import random

def son_top(x = 10):
    print("\nMen son o'yladim. Uni topa olasizmi?")
    tasodifiy_son = random.randint(1, x)
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input("\n>>>"))
        if taxmin > tasodifiy_son:
            print("\nMen o'ylagan son kichikroq.")
        elif taxmin < tasodifiy_son:
            print("\nMen o'ylagan son kattaroq.")
        else:
            print(f"\n{taxminlar}ta taxmin bilan topdingiz!")
            break
    return taxminlar

def son_oyla(x = 10):
    input("\nEndi siz son o'ylang, men esa topishga harakat qilaman. Davom etish uchun istalgan tugmani bosing. ")
    taxminlar = 0
    
    quyi = 1
    yuqori = x 
    while True:
        taxminlar += 1
        if quyi != yuqori:
            pc_son = random.randint(quyi, yuqori)
        else:
            pc_son = quyi
        savol = input(f"\nSiz {pc_son} sonini o'yladingiz. To'g'ri topdim (t), men o'ylagan son kattaroq (+), kichikroq (-) : ")
        if savol == '+':
            quyi = pc_son + 1
        elif savol == '-':
            yuqori = pc_son - 1
        else:
            print(f"\nMen {taxminlar}ta taxmin bilan topdim topdim!")
            break
    return taxminlar


def play(x = 10):
    yana = True
    while yana:
        taxmin_user = son_top()
        taxmin_pc = son_oyla()
        if taxmin_user > taxmin_pc:
            print("\nMen yutdim!")
        elif taxmin_user < taxmin_pc:
            print("\nSiz yutdingiz!")
        else:
            print("\nDurrang!")
        yana = int(input("\nYana o'ynashni xohlaysizmi? ha(1)/yo'q(0) : "))
    
play()       
    
        
    
    
            
    