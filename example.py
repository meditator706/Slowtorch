from Slowtorch import Variable
import numpy as np


x = Variable(np.array(1.0))
y = 3*x**2+9*x-x**3
z = y / (y+2)
z.backward()

print(x.grad)
