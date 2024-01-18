
.. _deploy:

Deploying to the robot
----------------------

.. contents:: :local:

The easiest way to install code on the robot is to use the deploy command
provided by pyfrc. This command will first run any unit tests on your robot
code, and if they pass then it will upload the robot code to the roboRIO.
Running the tests is really important, it allows you to catch errors in your
code before you run it on the robot. 

1. Make sure you have RobotPy installed on the robot (:ref:`RobotPy install guide <install_robotpy>`) and on your computer
2. Once that is done, you can just run the following command and it will upload the code and start it immediately.

.. tab:: Windows

   .. code-block:: sh

      py -3 -m robotpy deploy

.. tab:: Linux/macOS

   .. code-block:: sh

      python3 -m robotpy deploy

You can watch your robot code's output (and see any problems) by using the
netconsole program (you can either use NI's tool, or `pynetconsole <https://github.com/robotpy/pynetconsole>`_.
You can use netconsole and the normal FRC tools to interact with the running
robot code.

If you're having problems deploying code to the robot, check out the
:ref:`troubleshooting section <troubleshooting>`

Immediate feedback via Netconsole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that when you run the deploy command like that, you won't get any feedback
from the robot whether your code actually worked or not. If you want to see the
feedback from your robot without launching a separate NetConsole window, a
really useful option is ``--nc``. This will cause the deploy command to show
your program's console output, by launching a netconsole listener.

.. tab:: Windows

   .. code-block:: sh

      py -3 -m robotpy deploy --nc

.. tab:: Linux/macOS

   .. code-block:: sh

      python3 -m robotpy deploy --nc

.. note:: This requires the driver station software to be connected to your robot

Skipping Tests
~~~~~~~~~~~~~~

Now perhaps your tests are failing, but you really need to upload the code, and
don't care about the tests. That's OK, you can still upload code to the robot:

.. tab:: Windows

   .. code-block:: sh

      py -3 -m robotpy deploy --skip-tests

.. tab:: Linux/macOS

   .. code-block:: sh

      python3 -m robotpy deploy --skip-tests

Starting deployed code at boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish for the deployed code to be started up when the roboRIO boots up,
you need to make sure that "Disable RT Startup App" is **not** checked in the
roboRIO's web configuration. See the
:doc:`FIRST documentation <frc:docs/software/roborio-info/roborio-web-dashboard>`
for more information.

Manually deploying code
~~~~~~~~~~~~~~~~~~~~~~~

Generally, you you just use the steps above. However, if you really want to,
then see :ref:`manual_code_deploy`.

Next Steps
~~~~~~~~~~

Let's talk about :ref:`the robot simulator <simulator>` next.

