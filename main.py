#!/usr/bin/python3

# imports the necessary libraries
import sys
import timer
import vex

# MOTORS
_claw = vex.Motor(2)
_forwardLeft = vex.Motor(3, True)
_forwardRight = vex.Motor(4)
_wrist = vex.Motor(5)
_backRight = vex.Motor(6)
_backLeft = vex.Motor(7, True)


# JOYSTICK
joystick = vex.Joystick()
joystick.set_deadband(15)


# VARIBALES
# global variables

AUTO_TIME = 5
WRIST_UP_POWER = 50
WRIST_DOWN_POWER = -(50)
CLAW_CLOSE_POWER = 50
CLAW_OPEN_POWER = -(50)
CLAW_CONSTANT_CLOSE_POWER = 10


def CLAW_DRIVE():
    # timer variables
    tickTimer = timer.Timer()
    tickTimer_max = 1.3    # Seconds
    tickTimer.start()
    buttonTimer = timer.Timer()
    buttonTimer_max = 1.3  # Seconds
    buttonTimer.start()
    clawIsOpen = False

    while True:
        # print 'TELEOP CLAW'
        # CLAW MOTORS
        if joystick.b8down() and buttonTimer.elapsed_time() > buttonTimer_max:
            if not clawIsOpen:
                clawIsOpen = True
                # RESET TICK TIMER
                tickTimer.start_lap()

            elif clawIsOpen:
                clawIsOpen = False
                # RESET TICK TIMER
                tickTimer.start_lap()

            # RESET BUTTON TIMER
            buttonTimer.start_lap()

        if tickTimer.elapsed_time() < tickTimer_max:
            if not clawIsOpen:
                # IF CLAW IS CLOSED OPEN IT
                _claw.run(CLAW_OPEN_POWER)

            elif clawIsOpen:
                # IF CLAW IS OPEN CLOSE IT
                _claw.run(CLAW_CLOSE_POWER)

        # CONTINIOUS POWER TO CLOSE THE CLAW
        else:
            if clawIsOpen:
                # IF CLAW IS OPEN PROVIDE CONTANT POWER TO THE MOTOR
                _claw.run(CLAW_CONSTANT_CLOSE_POWER)
            else:
                # TURNS OFF CLAW IF IT'S OPEN
                _claw.off()


def BASE_DRIVE():
    while True:
        # print 'TELEOP BASE'
        # BASE MOTORS
        # ARCADE DRIVE
        forward = joystick.axis3()
        steer = joystick.axis4()

        # calculate left and right power
        left = forward + steer
        right = forward - steer

        # LEFT DRIVE
        _forwardLeft.run(left)
        _backLeft.run(left)
        # RIGHT DRIVE
        _forwardRight.run(right)
        _backRight.run(right)


def WRIST_DRIVE():
    while True:
        # print 'TELEOP WRIST'
        # WRIST MOTORS
        if joystick.b5up():
            _wrist.run(WRIST_DOWN_POWER)
        elif joystick.b5down():
            _wrist.run(WRIST_UP_POWER)
        else:
            _wrist.off()


def autonomous():
    import random
    lef_choice = random.choice([-50, 50])
    rig_choice = lef_choice * -1
    print(rig_choice)
    while True:
        _backLeft.run(lef_choice)
        _forwardLeft.run(lef_choice)
        _backRight.run(rig_choice)
        _forwardRight.run(rig_choice)
        # print "AUTO", sys.clock()
        if AUTO_TIME < sys.clock():
            print('AUTO FINISHED')
            break


def driver():
    print("TELEOP running")
    sys.run_in_thread(CLAW_DRIVE)
    sys.run_in_thread(BASE_DRIVE)
    sys.run_in_thread(WRIST_DRIVE)


# print(autonomous())
autonomous()
driver()