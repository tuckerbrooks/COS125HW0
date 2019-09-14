# File: hw1b.py
# Author: Tucker Brooks
# Date: September 14, 2019
# Section: 1001
# E-mail: tucker.brooks@maine.edu
# Description:
# Buying ice cream
# Collaboration:
# N/A

price = input("How much is this ice cream bar? ")
total_cost = round(float(price) * 1.055 * 3, 2)
print ("I would like three bars. Here is $", str(total_cost), ".")
print ("Thank you")