import matplotlib.pyplot as plot

numlist = [8, 6, 5, 3]
namelist = ['sevies', 'sophomores', 'juniors L', 'seniors']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.05, 0.0, 1, 0.02]

plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')

