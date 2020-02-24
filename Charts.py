import matplotlib.pyplot as plt
import time

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y, 'h', color="red")
plt.title("Sample PLot")
plt.xlabel("Time")
plt.ylabel("Number of attendances")

plt.show()
