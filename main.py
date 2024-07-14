import matplotlib.pyplot as plt
import math

a = 0.8
b = -2.5
c = 20

times = []
temperatures = []

for i in range(5):
  time = float(input("Enter the time: "))
  if time > 12:
    print("Time should be less than 12 hours.")
    break
  times.append(time)
  temperature = a * time * time + b * time + c
  temperatures.append(temperature)

plt.plot(times, temperatures, marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel("Temperature")
plt.title('Weather model')
plt.grid(True)
plt.show()