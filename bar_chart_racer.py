from bar import Bar

file = open("infinity-war.txt")
title = file.readline().strip()
x_lable = file.readline().strip()
source = file.readline().strip()

file.readline()

bars = {}

for line in file:
    line = line.strip()
    if line !="":
        period,name,detail,value,catagory = line.split(",")
        value = int(value)
        bar = Bar(name,value,catagory)
        if period not in bars:
            bars[period] = []
        bars[period].append(bar)
file.close()
periods = sorted(bars)