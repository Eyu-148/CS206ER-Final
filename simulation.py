from robot import ROBOT
from world import WORLD
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import matplotlib.pyplot as plt

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self, sleepTime):
        for t in range(0,c.maxTimeStep):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act()
           # get the height at each timestep
            '''basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot.robotId)
            basePosition = basePositionAndOrientation[0]
            zPosition = basePosition[2]
            self.robot.height[t] = zPosition'''
            #print(t)
            time.sleep(float(sleepTime))

    # method to save the sensor value for specific robot/simulation
    def Get_Footprint(self):
        with open("data/footprintB.txt", 'a') as f:
            for t in range(0, c.maxTimeStep):
                f.write(str(self.robot.sensors['LeftFeet'].sensorValues[t]) + " " + str(self.robot.sensors['FrontFeet'].sensorValues[t]) 
                        + " " + str(self.robot.sensors['BackFeet'].sensorValues[t]) + " " + str(self.robot.sensors['RightFeet'].sensorValues[t]) + '\n')

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()