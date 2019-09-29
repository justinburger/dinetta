# Dinetta
IP Camera Object Detection, Training and Alerting

## Project Objectives
Provide a simple to use object (person) dectection, training and alerting system that will run on a raspberry pi, pulling images from multiple IP Cameras for near realtime alerting.

**Functionality Goals**
+ User Defined Settings:
    + Alerting
        + How often to see consider a detection as the same event.
        + Where to email on detection (differnt ones for differnt detections)
        + What % likleyhood to alert on
        + How many Different camera sources to alert on.
        + Different settings per time of day.
        + Different alerting schedules for differnt types (immedate, per day/per week)
        + How many training images to store before rotating.
    + Off device storage options (S3)
    
+ Web based UI to select objects on still frame images used for training object detection.

## Project Componets

### Image Capture Service
``./manage image_capture_service [--all]
``

The Image Capture Service provides the functionality to pull still images 
from defined IP Cameras via RTSP.


### Image Trainer
Provides the front/backend needed to work thru stored images while training.


