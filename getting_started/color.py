from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Create EV3 object
ev3 = EV3Brick()

#set up motor
left_motor  = Motor(Port.A)right_motor = Motor(Port.D)

#Set up color sensor
color_sensor = ColorSensor(Port.S1)

#Create robot drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Bep 
ev3.speaker.beep()

base_speed = -120
turn_rate = 80
threshold = 20

while True:
    light = color_sensor.reflection()

    if light < threshold:
        # On black → turn slightly LEFT
        robot.drive(base_speed, -turn_rate)
    else:
        # On white → turn slightly RIGHT
        robot.drive(base_speed, turn_rate)
    wait(20)