.. Configuration Guide
   07/22/24
   Abhishekh Reddy

   Sections hierarchy reference:
      Level 1: ====
      Level 2: ----
      Level 3: ''''
..

Configuration Guide
==========================

Configuration File
------------------

The software uses a YAML file to read and store tracking and calibration parameters. Configuration
file is needed to provide marker specifications for tracking and calibration modes and for saving
the intrinsic parameters from calibration. It needs to be generated and customized for the first
time.

.. code-block:: yaml
   :name: config-structure
   :caption: Structure of the configuration YAML file.

   marker_detection:
      camera_id: Integer
      frame_width_pixels: Integer
      frame_height_pixels: Integer
      frame_rate_fps: Integer
      show_rejected_markers: Boolean integer (0/1)

   line_follower_marker:
      marker_side_meters: Float
      marker_id: Integer
      marker_dictionary_id: Integer - As per aruco::PREDEFINED_DICTIONARY_NAME

   board_markers:
      marker_side_meters: Float
      marker_seperation_meters_x: Float
      marker_seperation_meters_y: Float
      marker_ids: [ Array of integers ]
      marker_dictionary_id: Integer - As per aruco::PREDEFINED_DICTIONARY_NAME

   track_selection: Integer - As per options::TrackSelection

   line_track:
      point1:
         x_meters: Float
         y_meters: Float
      point2:
         x_meters: Float
         y_meters: Float

   round_track:
      center:
         x_meters: Float
         y_meters: Float
      width_meters: Float
      height_meters: Float

   camera_calibration:
      marker_side_meters: Float
      square_side_meters: Float
      squares_quantity_x: Integer
      squares_quantity_y: Integer
      marker_dictionary_id: Integer - As per aruco::PREDEFINED_DICTIONARY_NAME
      camera_matrix: !!opencv-matrix
         rows: Integer (Auto-generated)
         cols: Integer (Auto-generated)
         dt: Character (Auto-generated)
         data: [ Array of floats ] (Auto-generated)
      distortion_coefficients: !!opencv-matrix
         rows: Integer (Auto-generated)
         cols: Integer (Auto-generated)
         dt: Character (Auto-generated)
         data: [ Array of floats ] (Auto-generated)


``marker_detection``
''''''''''''''''''''

Parameters in this section apply for both tracking and calibration modes. Mostly consists of
camera settings and one fiducial marker detection setting used in Tracking and Calibration modes.

.. important::

   The ``frame_width_pixels`` and ``frame_height_pixels`` settings **must** remain
   the same before and after the camera calibration. Since the camera intrinsic parameters change
   with the image size used in calibration, make sure to re-calibrate the camera if a new
   frame size were to be used for tracking.

Setting up the ``camera_id`` field
   This number corresponds to the number at the end assigned to the device folder for the camera
   in the ``/dev`` directory.

   If there is only one camera connected to the computer, the folder in the ``/dev`` tree would
   usually be ``/dev/video0`` and the ``camera_id`` field will be ``0``.

   If there are multiple cameras connected to the computer (Such as an external camera connected
   to a laptop with an in-built webcam), the program can pick one of them to use based on the
   value in this field.

   The correct device folder in the ``/dev`` directory for the desired camera can be looked up
   using the ``v4l2-ctl`` command in :numref:`list-webcams-command`.

   .. code-block:: bash
      :name: list-webcams-command
      :caption: Terminal command for listing the connected webcams with their device folders

      v4l2-ctl --list-devices

``line_follower_marker``
''''''''''''''''''''''''

Specifies the size, ID and dictionary of the fiducial marker that will be mounted on the line
following robot.

.. TODO: Insert a diagram here with dimensions as fields in this section

``board_markers``
'''''''''''''''''

Specifies the size, ID and dictionary of the fiducial markers at the four corners of the track
board. The program treats these markers as a single combination and gives the pose from the
**third marker ID** in the ``marker_ids`` field.

.. TODO: Insert a diagram here with dimensions as fields in this section

.. tip::

   The values for ``marker_dictionary_id`` in the above two sections are based on the
   `aruco::PREDEFINED::DICTIONARY_NAME`_ enum defined in the libary.
   :numref:`dictionary-enum-table` lists the values for reference.


.. table:: List of marker dictionaries with their corresponding enum values
   :name: dictionary-enum-table
   :widths: grid
   :align: center

   =================  ========  =====
   Dictionary         Quantity  Value
   =================  ========  =====
   4 x 4              50        0
   4 x 4              100       1
   4 x 4              250       2
   4 x 4              1000      3
   5 x 5              50        4
   5 x 5              100       5
   5 x 5              250       6
   5 x 5              1000      7
   6 x 6              50        8
   6 x 6              100       9
   6 x 6              250       10
   6 x 6              1000      11
   7 x 7              50        12
   7 x 7              100       13
   7 x 7              250       14
   7 x 7              1000      15
   ArUco Original     1024      16
   AprilTag tag16h5   30        17
   AprilTag tag25h9   35        18
   AprilTag tag36h10  2320      19
   AprilTag tag36h11  587       20
   AprilTag tag36h12  250       21
   =================  ========  =====

``track_selection``
'''''''''''''''''''

The software currently supports tracking for straight line and round tracks. Only one type of track
can be used at a single time. To use a different type of track, change this field and restart the
program. The values are based on `options::TrackSelection`_ enum.

.. TODO: Finish the remaining sections.

.. LINK REFERENCES ---------------------------------------------------------------------------------
.. _aruco::PREDEFINED::DICTIONARY_NAME: https://docs.opencv.org/3.4/dc/df7/dictionary_8hpp.html
.. _options::TrackSelection: https://docs.opencv.org/3.4/dc/df7/dictionary_8hpp.html
