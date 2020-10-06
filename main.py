# Created by: Mr. Coxall
# Created on: Oct 2020
#
# This program calculates the cost of a pizza, give the diameter

# price constants
LABOUR = 0.75
RENT = 1.0
PRICE_PER_INCH_DIAMETER = 0.50
HST = 1.13

sub_total = 0.00
total = 0.00
diameter = 0.00

# input
diameter = input("Enter the diameter of the pizza you would like (inch): ")
diameter = float(diameter)
# process 
sub_total = LABOUR + RENT + (PRICE_PER_INCH_DIAMETER * diameter)
total = sub_total * HST
# round off
total = round(total, 2)
# output
print("The cost for a " + str(diameter) + "inch pizza is $" + str(total))