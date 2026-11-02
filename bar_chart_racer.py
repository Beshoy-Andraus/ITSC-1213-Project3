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


from bar_chart import BarChart

k=10
chrt = BarChart(title, x_lable, source)
for period in periods:
    ranked = sorted(bars[period], reverse=True)
    top = ranked[:k]
    chrt.reset()
    chrt.set_caption(period)
    for bar in top:
        chrt.add(bar.get_name(), bar.get_value(), bar.get_catagory())
    chrt.draw()
    chrt.pause(0.01)
chrt.leave_window_open()