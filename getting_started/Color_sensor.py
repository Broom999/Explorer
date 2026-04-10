#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor  = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

color_sensor = ColorSensor(Port.S1)

ev3.speaker.beep()

threshold = 20

while True:
    light = color_sensor.reflection()

    if light < threshold:
        # On black → turn slightly LEFT                            
        robot.drive(-90, 60)
    else:
        # On white → turn slightly RIGHT

        robot.drive(-90, -60)