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

# Drive forward until the sensor sees a dark surface.
while True:
    light = color_sensor.reflection()

    while light > 2:
        robot.stop()
        ev3.speaker.beep(880, 300)
        break
    else:
        robot.drive(-100, 0)

    wait(10)

ev3.screen.print("Dark line found!")
ev3.screen.print("Light: " + str(light))