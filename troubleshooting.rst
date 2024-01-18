
.. _troubleshooting:

Troubleshooting
===============

.. contents:: :local:

Robot Code
----------

Problem: I can't run code on the robot!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are lots of things that can go wrong here. It is very important to have
the latest versions of the FIRST robot software installed:

* Robot Image
* Driver Station + Tools

The `FIRST WPILib documentation <https://docs.wpilib.org>`_
contains information on what the current versions are, and how to go about
updating the software.

You should also have the latest version of the RobotPy software packages:

* Do you have the latest version of pyfrc?

.. warning:: Make sure that the version of WPILib on your computer matches the
   version installed on the robot! You can check what version you have locally
   by running

   .. tab:: Windows

      .. code-block:: sh

         py -3 -m pip list

   .. tab:: Linux/macOS

      .. code-block:: sh

         pip3 list

1. Did you run the deploy command to put the code on the robot?
2. Make sure you have the latest version of pyfrc! Older versions **won't** work.
3. Read any error messages that pyfrc might give you. They might be useful. :)

Problem: no module named 'wpilib'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're on your local computer, did you :ref:`install robotpy via pip <install_computer>`?

If you're on the roboRIO, did you :ref:`install RobotPy <install_robotpy>`?

Problem: no module named ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a non-WPILib vendor library, it must be installed separately.

* :ref:`robotpy_components`


If you're on your local computer, did you :ref:`install robotpy via pip <install_computer>`?

If you're on the roboRIO, did you :ref:`install RobotPy <install_robotpy>`?

Problem: deploy cannot connect to the robot, or appears to hang
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Can you ping your robot from the machine that you're deploying code from? If not, the deploy process isn't going to be able to connect to the robot either.
2. Try to ssh into your robot, using `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_ or the ``ssh`` command on Linux/macOS. The username to use is ``lvuser``, and the password is an empty string. If this doesn't work, the deploy process won't be able to copy files to your robot
3. If all of that works, it might just be that you typed the wrong hostname to connect to. Delete ``.wpilib/wpilib_preferences.json``, and try again.


Problem: I deploy successfully, but the driver station still shows 'No Robot Code'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Did you use the ``--nc`` option to the deploy command? Your code may have crashed, and the output should be visible on netconsole.
2. If you can't see any useful output there, then ssh into the robot and run ``ps -Af | grep python3``. If nothing shows up, it means your python code crashed and you'll need to debug it. Try running it manually on the robot using this command:: 
    
    python3 /home/lvuser/py/robot.py run

Problem: My code segfaulted and there's no Python stack trace!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you find something like this here's what you can do:

First, figure out where the code is crashing. Traditional debugging techniques
apply here, but a simple way is to just delete and/or comment out things until
it no longer fails. Then add the last thing back in and verify that the code 
still crashes.

Advanced users can compile a custom version of the robotpy libraries with
symbols and use gdb to get a full stack trace (documentation TBD).

Once you've identified where it crashes, file a bug on github and we can help
you out.

Common causes
^^^^^^^^^^^^^

Python objects are reference counted, and sometimes when you pass one directly
to a C++ function without retaining a reference a crash can occur::

    class Foo:
        def do_something(self):
            some_function(Thing())

In this example, ``Thing`` is immediately destroyed after some_function returns
(because there are no references to it), but some_function (or something else)
tries to use the object after it is destroyed. This causes a segfault or memory
access exception of some kind.

These are considered bugs in RobotPy code and if you report an issue on github
we can fix it. However, as a workaround you can retain a reference to the thing
that you created and that often resolves the issue::

    class Foo:
        def do_something(self):
            self.thing = Thing()
            some_function(self.thing)

.. _troubleshooting_nt:

pyntcore
--------

isConnected() returns False!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keep in mind that NetworkTables does not immediately connect, and it will
connect/disconnect as devices come up and down. For example, if your program
initializes NetworkTables, sends a value, and exits -- that almost certainly
will fail.

Ensure you're using the correct mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're running NetworkTables as part of a RobotPy robot -- relax,
NetworkTables is setup as a server automatically for you, just like in
WPILib!

If you're trying to connect to the robot from a coprocessor (such as a
Raspberry Pi) or from the driver station, then you will need to ensure that
you initialize NetworkTables correctly. The following shows how to initialize
pyntcore correctly as a client.

.. code-block:: python

    import ntcore

    inst = ntcore.NetworkTableInstance.getDefault()

    # start a NT4 client
    inst.startClient4("example client")

    # connect to a roboRIO with team number TEAM
    inst.setServerTeam(TEAM)

    # starting a DS client will try to get the roboRIO address from the DS application
    inst.startDSClient()

    # connect to a specific host/port
    inst.setServer("host", ntcore.NetworkTableInstance.kDefaultPort4)

Don't know what the right hostname is? That's what the next section is for...

Use static IPs when using NetworkTables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso:: :ref:`networktables_guide`


Problem: I can't determine if NetworkTables has connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that you have enabled python logging (it's not enabled by default)::
   
   # To see messages from networktables, you must setup logging
   import logging
   logging.basicConfig(level=logging.DEBUG)

Once you've enabled logging, look for messages that look like this::

    INFO:nt:CONNECTED 10.14.18.2 port 40162 (...)

If you see a message like this, it means that your client has connected to the
robot successfully. If you don't see it, that means there's still a problem.
Much of the time this occurs when not using a static IP for your robot, and is
fixed when you start using a static IP for your robot.

.. _troubleshooting_cscore:

cscore
------

Problem: I can't view my cscore stream via a dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, make sure that your stream is actually working. Connect with a web
browser to the host that the stream is running on on the correct port (if
you are using CameraServer, this will be output via a python logging
message). The default port is 1181.  

The LabVIEW dashboard and Shuffleboard both receive information about
connecting to the stream via NetworkTables. This means that both your
cscore code and the dashboard need to be connected to your robot, and your
robot's code needs to be running. If you have python logging enabled,
then your cscore code should output a message like this if it's connected
to a robot::

    INFO:nt:CONNECTED 10.14.18.2 port 40162 (...)

If it's connected to NetworkTables, then you can use something like the
TableViewer to view the contents of NetworkTables and see if the correct
URL is being published. Look under the 'CameraPublisher' key.

Problem: My image processing code is running at 100% CPU usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should only encounter this if running your own image processing code. 
If you're just streaming a camera, this should never happen and is a bug.
When doing image processing, there's a few ways you can use too much
CPU, particularly if you do it on a RoboRIO. Here are some thoughts:

* Resizing images is really expensive, don't do that. Instead, set the
  resolution of your camera via the API provided by cscore
* Preallocate your image buffers. Most OpenCV functions will optionally take a
  final argument called 'dst' that it will write the result of the 
  image processing operation to. If you don't provide a 'dst' argument,
  then it will allocate a new image buffer each time. Because image buffers
  can be really large, this adds up quickly.
* Try a really small resolution like 160x120. Most image processing
  tasks for FRC are still perfectly doable at small resolutions. 
* If your framerate is over 10fps, consider bringing it down and see
  if that helps.

Problem: It still doesn't work!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please `file a bug on github <https://github.com/robotpy/robotpy-cscore/issues>`_
or use one of our :ref:`support channels <support>`.
