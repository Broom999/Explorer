#!/usr/bin/env pybricks-micropython
# ↑ This line MUST be the first line of every EV3 program you write.
# It tells the EV3 brick: "this file is a MicroPython program."
# If you delete it or move it, the program will not run.
# -------------------------------------------------------
# IMPORTS — loading the tools we need
# -------------------------------------------------------
from pybricks.hubs import EV3Brick
# ↑ "from X import Y" means: go to the pybricks library, find the hubs section,
# and bring in the EV3Brick tool.
# EV3Brick gives us control of the screen, speaker, and status light.
from pybricks.ev3devices import Motor
# ↑ From the ev3devices section, bring in Motor.
# We need this because our two wheels are driven by two Motor objects.
from pybricks.parameters import Port
# ↑ From parameters, bring in Port.
# Port lets us say *which plug* a motor is connected to: Port.B or Port.C.
# Without this, we can't tell the robot where to look for its motors.
from pybricks.robotics import DriveBase
# ↑ DriveBase is the main tool for this unit.
# It takes two motors and combines them into one "robot" object
# that can drive straight and turn without us doing the math ourselves.
from pybricks.tools import wait
# ↑ wait() pauses the program for a number of milliseconds.
# 1000 ms = 1 second. We use it to add pauses between moves.
# -------------------------------------------------------
# OBJECT CREATION — building the things we'll control
# -------------------------------------------------------
ev3 = EV3Brick()
# ↑ This creates an EV3Brick object and stores it in a variable called ev3.
# Remember from Unit 1: an *object* is a variable that represents a real
# physical thing. ev3.speaker, ev3.screen, ev3.light all work now.
left_motor = Motor(Port.D)
# ↑ This creates a Motor object for the motor plugged into Port B.
# We store it in a variable called left_motor so the name tells us
# which side of the robot it controls.
# Port.B is a constant — it means "the port labeled B on the brick."
right_motor = Motor(Port.C)
# ↑ Same thing, but for Port C, which controls the right wheel.
# Having separate left_motor and right_motor variables makes the
# next line easier to understand.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# ↑ This is the most important line in the setup.
# DriveBase() takes four arguments:
#
# left_motor → the motor object for the left wheel
# right_motor → the motor object for the right wheel
# wheel_diameter → the diameter of each wheel in millimeters (55.5 mm)
# axle_track → the distance between the two wheels in millimeters (104 mm)
#
# Why do we need the measurements?
# When we say robot.straight(500), DriveBase needs to calculate exactly
# how many times each wheel should rotate to travel 500 mm.
# It can only do that math if it knows how big the wheels are.
#
# If your wheel_diameter is wrong, the robot will travel the wrong distance.
# If your axle_track is wrong, the robot will turn the wrong amount.
# -------------------------------------------------------
# START SIGNAL
# -------------------------------------------------------
ev3.screen.clear()
# ↑ Clears anything left on the screen from a previous run.
ev3.screen.print("Ready!")
# ↑ Displays "Ready!" on the EV3 screen so we know the program started.
ev3.speaker.beep()
# ↑ Plays a short beep. This is a good habit — it confirms the program
# launched successfully before any movement begins.