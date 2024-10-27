# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:56:02 2024

@author: user
"""

import random
asoslar = ['tosh', 'qaychi', 'qog\'oz']
print("Tosh, qaychi, qog'oz o'yini.")
while True:
    asos = random.choice(asoslar)
    user_asos = input(">>>")
    if user_asos == asos:
        win = 1
    elif user_asos == 'tosh' and asos == 'qaychi':
        win = 2
    elif user_asos == 'tosh' and asos == 'qog\'oz':
        win = 3
    elif user_asos == 'qaychi' and asos == 'tosh':
        win = 3
    elif user_asos == 'qaychi' and asos == 'qog\'oz':
        win = 2
    elif user_asos == 'qog\'oz' and asos == 'tosh':
        win = 2
    elif user_asos == 'qog\'oz' and asos == 'qaychi':
        win = 3
    elif user_asos == 'quit':
        break
    print(f"{asos}")  
    if win == 2:
        print("Siz yutdingiz!")
    elif win == 1:
        print("Durrang!")
    else:
        print("Yutqazdingiz!")
