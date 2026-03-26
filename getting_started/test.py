#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

ev3.screen.print("Left motor")
left_motor.run_angle(300, 360)
wait(1000)

ev3.screen.clear()
ev3.screen.print("Right motor")
right_motor.run_angle(300, 360)