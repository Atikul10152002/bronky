#!/usr/bin/python3

'''
imports the necessary libraries
'''
# import sys
import vex
import timer

'''
Initializes the Motor, Joystick, and Sensor variables.
Each motor is connected to a port on the microcontroller.
The port # in .Motor(#) is the port number.
These variables are called / used by later functions.
'''


# MOTORS
__robotName__ = 'Bronky'
_claw = vex.Motor(2)
_forwardLeft = vex.Motor(3, True)
_forwardRight = vex.Motor(4)
_wrist = vex.Motor(5)
_backRight = vex.Motor(6)
_backLeft = vex.Motor(7, True)

# JOYSTICK
joystick = vex.Joystick()
joystick.set_deadband(10)


def run():
    '''
    Runs the program
    '''
    driver()
    # vex.run_autonomous(autonomous)
    # vex.run_driver(driver)


def autonomous():
    pass


def leftDrive(power):
    
    '''
    Controls the left motors
    Takes joystick axis as parameter
    '''
    _forwardLeft.run(power)
    _backLeft.run(power)

    # left_base_motor.run(joystick.axis3())
    # motor_7.run(joystick.axis3())


def rightDrive(power):
    '''
    Controls the right motors
    Takes joystick axis as parameter
    '''
    _forwardRight.run(power)
    _backRight.run(power)

    # right_base_motor.run(joystick.axis2())
    # motor_6.run(joystick.axis2())


def tankDrive(leftAxis, rightAxis):
    '''
    tank drive
    takes the left and right axis as prarameter
    '''
    leftDrive(leftAxis)
    rightDrive(rightAxis)


def arcadeDrive(forwardAxis, SteerAxis):
    '''
    arcade drive
    takes the forward and steer axis as prarameter
    '''
    forward = forwardAxis
    # forward = - forwardAxis
    steer = SteerAxis

    # calculate left and right power
    left = forward + steer
    right = forward - steer

    # apply power to motors
    leftDrive(left)
    rightDrive(right)


def baseRun():
    # base left axis 3
    # base right axis 2
    tankDrive(joystick.axis3(), joystick.axis2())


def wristRun():
    # wrist b5
    if joystick.b5up():
        _wrist.run(-70)
    elif joystick.b5down():
        _wrist.run(70)
    else:
        _wrist.off()


def clawRun():
    # claw b8 ++ tick timer

    # timer = 201
    # buttonTimer = 100
    # clawIsOpen = False

    # if joystick.b8down() and buttonTimer > 100:
    #     if clawIsOpen:
    #         clawIsOpen = False
    #         timer = 0
    #     elif clawIsOpen is False:
    #         clawIsOpen = True
    #         timer = 0
    #     buttonTimer = 0 

    # if timer < 200:
    #     timer += 1
    #     if clawIsOpen:
    #         _claw.run(-50)
    #     elif clawIsOpen is False:
    #         _claw.run(50)
    # elif timer >= 200:
    #     _claw.off()

    # # applies continued closing force

    # # elif timer >= 200 and clawIsOpen == False:
    # #     claw_motor.run(-30)

    # if buttonTimer <= 100:
    #     buttonTimer += 1
    # if timer >= 250:
    #     timer = 0


    # claw b8 ++ is close and is open
    # tickTimer = timer.Timer()
    # tickTimer_max = 2
    # tickTimer.start()
    # buttonTimer = timer.Timer()
    # buttonTimer_max = 1
    # buttonTimer.start()
    # timer_stopping_point = 10
    # claw = False
    # open = True
    # closed = False

    # if joystick.b8down() and buttonTimer > buttonTimer_max:
    #     if claw is open:
    #         claw = closed
    #         tickTimer.reset()
    #     elif claw is closed:
    #         claw = open
    #         tickTimer.reset()
    #     buttonTimer.reset()

    # if tickTimer < tickTimer_max:
    #     if claw is open:
    #         _claw.run(-50)
    #     elif claw is closed:
    #         _claw.run(50)
    # elif tickTimer >= tickTimer_max:
    #     _claw.off()

    # # applies continued closing force

    # # elif timer >= 200 and clawIsOpen == False:
    # #     claw_motor.run(-30)

    # if tickTimer > timer_stopping_point:
    #     tickTimer.reset()
    # elif buttonTimer > timer_stopping_point:
    #     buttonTimer.reset()

    # claw b8 ++ timer module
    tickTimer = timer.Timer()
    tickTimer_max = 2
    tickTimer.start()
    buttonTimer = timer.Timer()
    buttonTimer_max = 1
    buttonTimer.start()
    timer_stopping_point = 10
    clawIsOpen = False

    if joystick.b8down() and buttonTimer > buttonTimer_max:
        if clawIsOpen:
            clawIsOpen = False
            tickTimer.reset()
        elif clawIsOpen is False:
            clawIsOpen = True
            tickTimer.reset()
        buttonTimer.reset()

    if tickTimer < tickTimer_max:
        if clawIsOpen:
            _claw.run(-50)
        elif clawIsOpen is False:
            _claw.run(50)
    elif tickTimer >= tickTimer_max:
        _claw.off()

    # # applies continued closing force

    # elif timer >= 200 and clawIsOpen == False:
    #     claw_motor.run(-30)

    if tickTimer > timer_stopping_point:
        tickTimer.reset()
    elif buttonTimer > timer_stopping_point:
        buttonTimer.reset()


def driver():
    '''
    User defined Logic
    '''

    while True:
        baseRun()
        wristRun()
        clawRun()

# run()