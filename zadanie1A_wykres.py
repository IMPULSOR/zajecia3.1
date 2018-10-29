import pylab

x = pylab.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(raw_input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

pylab.plot(x, y1)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()