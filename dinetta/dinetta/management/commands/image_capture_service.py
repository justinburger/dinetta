from django.core.management.base import BaseCommand, CommandError
import cv2

from colorama import init
from termcolor import colored

from injest.models import Camera
from injest.models import CameraGroup

class Command(BaseCommand):
    help = 'Captures images from an RTSP IP Camera'


    def handle(self, *args, **options):
        init()

        print(colored('Dinetta Image Capture Service ', 'white', 'on_red'))
        print(colored('Loading IP Camera List.... ', 'white'))
        cameras = Camera.objects.all()

        if len(cameras) < 1:
            print(colored('No IP Cameras Defined.. ', 'red'))
            return

        count = 0

        for camera in cameras:
            print(colored('Connecting to %s ....' % camera.label, 'white'))
            count += 1
            vidcap = cv2.VideoCapture(camera.connection_string)
            print(colored('Capturing Image from %s ....' % camera.label, 'white'))
            success, image = vidcap.read()
            if success:
                cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file

        return
