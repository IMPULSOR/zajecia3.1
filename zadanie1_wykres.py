from pylab import *

a = 1
b = 2
x = range(-10, 11)
y = []
for i in x:
    y.append(a * i + b)
plot(x, y)
title('Wykres f(x) = a*x - b')
grid(True)
show()