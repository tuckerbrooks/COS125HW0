# File: hw1b.py
# Author: Tucker Brooks
# Date: September 14, 2019
# Section: 1001
# E-mail: tucker.brooks@maine.edu
# Description:
# Get the sum of 10 numbers
# Collaboration:
# N/A

x = 0
total = 0
while (x < 10):
    value = input("Enter a value: ")
    total = total + int(value)
    x = x + 1
print ("The sum is:", total)