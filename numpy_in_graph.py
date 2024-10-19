import numpy as np
import matplotlib.pyplot as plt
x = np.array([5,10,15,20,25,30,35,40])
y = np.array([1,2,3,4,5,6,7,8])
plt.plot(x,y)
plt.title("Sports Watch Data")
plt.xlabel("Average pulse")
plt.ylabel("Calorie burnage")
plt.show()