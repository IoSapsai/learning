# 13 GPUS and 13 dongles
# other components = 1000BGN
# How long will it take to get back the invested money
# What will the initial investment be
# input:
#   Price of GPU
#   Price of dongle
#   Price of consumed electricity/day
#   Profit per GPU/day
# output:
#   Total money spent on the machine
#   Time to get back investment (rounded to the higher number)

import math

# input part
gpuPrice=(float(input("Price of a GPU")))*13
donglePrice=(float(input("Price of a dongle")))*13
electricityPrice=(float(input("Price of electricity/day")))*13
gpuProfit=(float(input("Profits per GPU")))*13

# output part

totalSpentParts = gpuPrice + donglePrice + 1000
dailyProfit = gpuProfit - electricityPrice
daystogetbackinvestment = math.ceil(totalSpentParts/dailyProfit)

print(f"The total money spent on the machine is {totalSpentParts} BGN.")
print(f"The machine will take {daystogetbackinvestment} days to return the investment.")