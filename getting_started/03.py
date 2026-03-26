#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ev3.screen.clear()
ev3.screen.print("Square!")
ev3.speaker.beep()
# A square has 4 sides and 4 corners.
# Instead of writing the same two lines 4 times, we use a loop.
robot.turn(45)
robot.straight(400)
ev3.screen.print("Loop begining!")
ev3.screen.clear()
for i in range(4):
# ↑ "for i in range(4)" means: repeat the indented block 4 times.
# i is a variable that counts the loops: 0, 1, 2, 3.
# range(4) generates the sequence [0, 1, 2, 3] — that's 4 values, 4 loops.
# We don't use i for anything here — it's just counting for us.
    robot.straight(600)
    robot.straight(-400)
# ↑ Drive 600 mm then go backwards 400 mm.
# This line is INDENTED — that means it's inside the loop.
# It will run once per loop iteration.
    robot.turn(90)
# ↑ Turn right 90 degrees to face the next side.
# Also inside the loop. After 4 iterations:
# - 4 straight moves × 400 mm = 1600 mm total driven
# - 4 turns × 90° = 360° total turning = back to start
    ev3.speaker.beep(880, 500)
    ev3.speaker.beep(500, 880) 
    ev3.screen.print("Done with loop" + str(i + 1))
# ↑ NOT indented — this is outside the loop.
# It runs once, after all 4 iterations are done.
robot.straight(-800)
robot.turn(-360)
ev3.screen.clear()
ev3.screen.print("Done!")
# ↑ Also outside the loop. Displays after the square is complete.