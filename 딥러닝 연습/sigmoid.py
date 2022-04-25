import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

x = np.arange(-10.0, 10.0, 0.1)
print(x)
y = sigmoid(x)
print(y)
fig = plt.figure(figsize = (8,7))
fig.set_facecolor('white')

plt.plot(x,y)
plt.ylim(-0.1, 10)
plt.xlim(-10, 10)
plt.title('Sigmoid',fontsize = 30)
plt.xlabel('x',fontsize = 20)
plt.ylabel('y', fontsize = 20)

plt.yticks([0,0, 0.5, 1,0])
plt.axvline(0.0, color = 'k')
ax = plt.gca()
ax.yaxis.grid(True)

plt.show()