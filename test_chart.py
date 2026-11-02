from bar_chart import BarChart

chart = BarChart("Game popularity", "Average active players", "Source: Fictional practice data")
chart.set_caption("2024")
chart.add("Space Builders", 1500, "Sandbox")
chart.add("Apex Arena", 1200, "Action")
chart.add("Turbo Track", 1000, "Racing")
chart.draw()
chart.pause(10) #this will keep the chart window visible/open for 10 seconds