import matplotlib.pyplot as plt
import constants as c
import numpy as np

# comparsion with testA/B
'''valueTestA = []
valueTestB = []
valueTestB2 = []
data1 = []
data2 = []
data3 = []
with open("data/testA.txt", 'r') as f1:
    for line in f1:
        data = line.split(" ")
        for i in range(c.populationSize):
            data1.append(float(data[i]))
        valueTestA.append(np.mean(data1))
with open("data/testB.txt", 'r') as f2:
    for line in f2:
        data = line.split(" ")
        for i in range(c.populationSize):
            data2.append(float(data[i]))
        valueTestB.append(np.mean(data2))
with open("data/testB_2.txt", 'r') as f2:
    for line in f2:
        data = line.split(" ")
        for i in range(c.populationSize):
            data3.append(float(data[i]))
        valueTestB2.append(np.mean(data3))

plt.plot(range(0, c.numberOfGenerations), valueTestA, label='testA')
plt.plot(range(0, c.numberOfGenerations), valueTestB, label='testB')
plt.plot(range(0, c.numberOfGenerations), valueTestB2, label='testB2')
plt.xlabel("generation")
plt.ylabel("avgrage distance")
plt.legend()
plt.show()'''

sensorLeft = []
sensorFront = []
sensorBack = []
sensorRight = []
with open("data/footprintA.txt", 'r') as f3:
    for line in f3:
        data3 = line.split(" ")
        if float(data3[0]) > 0:
            sensorLeft.append(float(data3[0]) + 2)
        else:
            sensorLeft.append(-1)
        if float(data3[1]) > 0:
            sensorFront.append(float(data3[1]) + 3)
        else:
            sensorFront.append(-1)
        if float(data3[2]) > 0:
            sensorBack.append(float(data3[2]))
        else:
            sensorBack.append(-1)
        if float(data3[3]) > 0:
            sensorRight.append(float(data3[3]) + 1)
        else:
            sensorRight.append(-1)

plt.scatter(range(0, c.maxTimeStep), sensorFront, label='front feet', s=0.5)
plt.scatter(range(0, c.maxTimeStep), sensorLeft, label='left feet', s=0.5)
plt.scatter(range(0, c.maxTimeStep), sensorRight, label='right feet', s=0.5)
plt.scatter(range(0, c.maxTimeStep), sensorBack, label='back feet', s=0.5)
plt.ylim(0, 4)
plt.legend()
plt.title("footprint of A")
plt.xlabel("timestep")
plt.ylabel("sensor values")
plt.show()
