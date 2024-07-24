.. Usage Guide
   07/23/24
   Abhishekh Reddy

   Sections hierarchy reference:
      Level 1: ====
      Level 2: ----
      Level 3: ''''
..

User Guide
===========

Quick Start
-----------

.. note::

   Before starting
      - Make sure that the program is compiled with the executable file ready to use.
      - Open a shell terminal in the directory where the executable is located. In Ubuntu, this can
        be done by pressing the ``CTRL + ALT + T`` keys and then specifying the path with the
        ``cd`` command.

The executable ``line-follower-tracker`` should be executed in a shell terminal with certain
argument flags. Use the boilerplate command from :numref:`tracking-boilerplate` and populate the
arguments with appropriate values to start the program in Tracking Mode.

.. code-block:: bash
   :caption: Terminal command for starting the program in Tracking Mode
   :name: tracking-boilerplate

   ./line-follower-tracker --config= --output= --name=

A window should pop up with the camera view showing detected markers. Press the ``SPACE`` key to
start/stop tracking and the ``ESC`` key to exit the program. Output results will be saved to the
given ``--output`` path before exiting.

Help Menu
---------

Running the executable in terminal without argument flags like in :numref:`execute-noargs` prints a
help menu with the list of available options and their brief descriptions as shown in
:numref:`executeoutput-noargs`.

.. code-block:: bash
   :caption: Terminal command without arguments
   :name: execute-noargs

   ./line-follower-tracker

.. code-block:: text
   :caption: Expected output from :numref:`execute-noargs`
   :name: executeoutput-noargs

   A configuration file is required for tracking.
   Line follower tracker using ArUco markers
   Usage: line-follower-tracker [params]

         --calibration (value:false)
                  Enable calibration mode
         --config
                  Configuration file path for the program
         --name
                  Name of the output
         --output
                  Output file directory for a new configuration file

Description of Options
----------------------

``--calibration``
''''''''''''''''''

Sets the mode of operation for the program in either Tracking or Calibration mode. Defaults to
``false`` if not specified which means the program always starts in Tracking Mode until
set to ``true`` for calibrating the camera.

:numref:`flag-combinations-table` shows the other valid combinations along with other flags.

.. table:: Valid combinations of other flags with \--calibration flag.
   :name: flag-combinations-table
   :widths: 6 8 8 8 50
   :align: center

   =====  ============  ============  ============  ================================================
   Value  Flag 1        Flag 2        Flag 3        Behavior
   =====  ============  ============  ============  ================================================
   true   \--output     None          None          Outputs a template configuration file with
                                                    defaults to this path with a
                                                    **timestamped name**.

   true   \--output     \--name       None          Outputs a template configuration file with
                                                    defaults to this path with the given
                                                    **custom name**.

   true   \--config     None          None          Starts the calibration window, **overwrites**
                                                    the new intrinsic parameters to this config file
                                                    after completion.

   true   \--config     \--output     None          Starts the calibration window, saves the
                                                    intrinsic parameters to a **new copy** of this
                                                    config file with a **timestamped name**.

   true   \--config     \--output     \--name       Starts the calibration window, saves the
                                                    intrinsic parameters to a **new copy** of this
                                                    config file with a given **custom name**.

   false  \--config     None          None          Starts the tracking window, any tracking results
                                                    will **not** be saved.

   false  \--config     \--output     None          Starts the tracking window, any tracking results
                                                    will be **saved** with the **timestamped name**.

   false  \--config     \--output     \--name       Starts the tracking window, any tracking results
                                                    will be **saved** with the given
                                                    **custom name**.
   =====  ============  ============  ============  ================================================

``--config``
''''''''''''

Sets the path to the configuration file which is needed to run the software. This needs to be
generated and configured before using the software for the first time and this is covered more in
detail in the :doc:`Configuration Guide` section.

``--name``
''''''''''

Sets the name for anything the program outputs (configuration files or tracking results). If not
specified, a timestamp in the format of ``YYYY-MM-DD-HH-MM-SS`` will be used as the name for the
output files/directory.

``--output``
''''''''''''

Sets the directory for the program to output any files (configuration files or tracking results).
This must be defined in Tracking mode to save the results. The influence of this flag is better
described in :numref:`flag-combinations-table`

.. LINK REFERENCES -------------------------------------------------------------
.. .. _<Link Name>: URL
