Eye Detection with Servo Motor Control
Overview

This project combines Python with OpenCV and an Arduino Uno to create a system that detects eyes through a webcam and moves a servo motor accordingly. When eyes are detected by the Python program, a signal is sent via serial communication to the Arduino, which controls the servo motor. The servo motor is connected to digital pin 4 on the Arduino.
Components Used

    Arduino Uno: The microcontroller used to control the servo motor.
    Python with OpenCV: For eye detection using the webcam and communication with the Arduino.
    Servo Motor: Moves in response to signals from the Arduino, based on the detection results.
    Arduino IDE: Used to upload the necessary code to the Arduino.
    Laptop/Webcam: Runs the Python script and provides the webcam feed.

Project Workflow

    The Python program detects eyes using the webcam and OpenCV.
    When eyes are detected, a signal is sent to the Arduino through serial communication.
    The Arduino receives the signal and moves the servo motor, which is connected to digital pin 4.

Hardware Setup

    Connect the servo motor's control wire to digital pin 4 on the Arduino.
    Connect the power and ground wires of the servo motor to the Arduino's 5V and GND pins.
    Connect the Arduino to the laptop via USB for serial communication.

Software Setup

    Use Python to detect eyes through the webcam and send signals to the Arduino.
    The Arduino code reads the serial input and moves the servo motor based on the received signal.
    The Arduino IDE is used to upload the code to the Arduino.

Usage

    Start the Python program to begin real-time eye detection through the webcam.
    When the system detects eyes, the servo motor will move in response.

Dependencies

    Python with OpenCV for eye detection.
    PySerial for communication between the laptop and Arduino.
    Arduino IDE for uploading code to the Arduino.

Future Enhancements

    Expand the project to control multiple servo motors.
    Integrate additional facial feature detection, such as smiles or head movement.
    Improve detection accuracy with a higher-quality camera.
