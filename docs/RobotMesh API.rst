RobotMesh API
=============

To program the VEX EDR (Cortex) controller:

  - Configure the peripherals connected to the controller in the "config" region. Create device objects in the vex module, passing the port number if necessary.

.. code-block:: Python
    
    import sys
    import vex
    #region config
    green_led = vex.DigitalOutput(1) # LED on Digital #1
    switch    = vex.DigitalInput(2)  # Switch on Digital #2
    motor     = vex.Motor(1)          # Motor on Motor #1
    #endregion

- Write Python code invoking methods on peripheral objects or the main module.

.. code-block:: Python

    green_led.on()      # Turn the LED on
    if switch.is_on():  # Check whether the switch is on
        print "Switch is on!"
    motor.run(50)       # Run the motor at 50% power
    sys.sleep(1)        # Sleep for 1 sec

- For details, see the full docs for the `vex <https://www.robotmesh.com/docs/vexcortex-python//html/namespacevex.html>`_ module

.. For any help with RobotMesh API:
      - refer to this `website <https://www.robotmesh.com/docs/vexcortex-python//html/index.html>`_


