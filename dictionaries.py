# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:48:34 2021

@author: kevmm
"""
trucks = dict()
trucks = {
    "brand": "Ford", 
    "model": "F100", 
    "year": "1978",
    "color": "Red"
    
    }
list1 = []
def NewList():
    num = int(input())
    while num != -1:
                num = int(input("Add next truck (-1 to quit) :"))
                list1.append(num)
                print(list1)
    if num != -1:
                list1.append(num)
                print(list1)
def printlist():
    print(list1)
    
def delete_element():
    print(list1)    
    choice = int(input("Which item to remove? (starts at 0!): "))
    list1.remove(choice)
def makeachange():
    print(trucks)
    colorchange = int(input("Change color to: "))
    white = int(input())
    black = 0
    red = 0
    if colorchange == red:
        print(trucks)
    elif colorchange == black:
        trucks["color"] = black
        print(trucks)
    elif colorchange == white:
        trucks["color"] = white
        print(trucks)
        
        
    
        
def listmenu():
        print("\n\n")
        print("1: Build list")
        print("2: Print list")
        print("3: Delete an element")
        print("4: Make a change")
        print("9 to exit")
        choice = int(input("Pick a number: "))
        return choice
    

ch = 2
while (ch != 9):
    ch = listmenu()
    if ch == 1:
        list1 = NewList()
    elif ch == 2:
            printlist()
    elif ch == 3:
            delete_element()
    elif ch == 4:
        makeachange()
        
 



