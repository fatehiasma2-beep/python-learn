# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:00:18 2026

@author: BabakMehr
"""



my_set_1 ={"asma","zahra","arash","ali"}
my_set_2 ={"ahmad","fatemhe","ali"}
print(my_set_1.union(my_set_2))
print(my_set_1.difference(my_set_2))
print(my_set_2.difference(my_set_1))
print(my_set_1.intersection(my_set_2))

print("ali" in my_set_1)
my_set_1.add("arsalan")
print(my_set_1)
my_set_1.update("reza")
print(my_set_1)
my_set_2.remove("fatemh")
print(my_set_2)
