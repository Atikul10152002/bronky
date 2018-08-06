
Bronky/vex.py
=================

.. automodule:: vex

.. class:: Motor (self, Port#)

   Takes the port number of the Motor as Parameter.

   .. method:: off ()

      Turn off.

   .. method:: run (self, power)

      Run at given power.

      Parameter: -100.0...100.0 (percent power).

   .. method:: run_raw	(self, power_raw)
      
      Run at given raw power.

      Parameters: -127.0...127.0 (raw power).


.. autoclass:: Joystick
   
   Config VexNet joystick

   .. method:: is_partner (self) -> bool

      True if this is a partner joystick, false if it is main joystick.

   .. method:: set_deadband	(self, value)		
      
      Set the deadband value for all axes (threshold below which axes would read out zero)

      Parameters: value	deadband threshold

   .. method:: axis1	(self) -> Returns number [-100...100]

      Position on axis 1: -100.0 to 100.0.

   .. method:: axis2	(self) -> Returns number [-100...100]

      Position on axis 2: -100.0 to 100.0.

   .. method:: axis3	(self) -> Returns number [-100...100]

      Position on axis 3: -100.0 to 100.0.

   .. method:: axis4	(self) -> Returns number [-100...100]

      Position on axis 4: -100.0 to 100.0.

   .. method:: accelX (self) -> bool	
      
      Accelerometer axis X: -100.0 to 100.0.

   .. method:: accelY (self) -> bool	
      
      Accelerometer axis Y: -100.0 to 100.0.

   .. method:: b5up	(self) -> bool	

      Button 5 pressed UP: True/False.

   .. method:: b5down(self) -> bool

      Button 5 pressed DOWN: True/False.

   .. method:: b6up(self) -> bool

      Button 6 pressed UP: True/False.

   .. method:: b6down(self) -> bool

      Button 6 pressed DOWN: True/False.

   .. method:: b7up(self) -> bool

      Button 7 pressed UP: True/False.

   .. method:: b7down(self) -> bool

      Button 7 pressed DOWN: True/False.

   .. method:: b7left(self) -> bool

      Button 7 pressed LEFT: True/False.

   .. method:: b7right(self) -> bool

      Button 7 pressed RIGHT: True/False.

   .. method:: b8up(self) -> bool

      Button 8 pressed UP: True/False.

   .. method:: b8down(self) -> bool

      Button 8 pressed DOWN: True/False.

   .. method:: b8left(self) -> bool

      Button 8 pressed LEFT: True/False.

   .. method:: b8right(self) -> bool

      Button 8 pressed RIGHT: True/False.

.. function:: battery_voltage() -> number

   Get main battery voltage, in volts.

.. function:: battery_backup_voltage()	-> number

   Get backup battery voltage, in volts.

.. function:: debug_output	(debug_output_type)	

   Set debug output type.

   debug_output_type: DebugOutput.AUTO|SERIAL|LCD|DISABLED

.. function:: run_driver( function )	

   Run the given function in a separate thread in DRIVER ONLY competition mode.
   
.. function:: run_autonomous(function)	

   Run the given function in a separate thread in AUTONOMOUS ONLY competition mode.

.. function:: competition_switch	()	 -> enum value (number)

   Returns state of the competition switch, as one of the constants in CompetitionSwitchState.




..   :undoc-members:
   :inherited-members:
   :private-members:
   :special-members:
   :members:
