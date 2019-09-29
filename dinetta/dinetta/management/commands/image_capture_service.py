from django.core.management.base import BaseCommand, CommandError
import cv2



class Command(BaseCommand):
    help = 'Captures images from an RTSP IP Camera'


    def handle(self, *args, **options):

        rtsp_server_url = 'rtsp://dev1:password@10.3.141.58/live'

        vidcap = cv2.VideoCapture(rtsp_server_url)
        success, image = vidcap.read()
        count = 0

        while success:
            cv2.imwrite("training_sets/no_people/frame%d.jpg" % count, image)  # save frame as JPEG file
            success, image = vidcap.read()
            count += 1
            self.stdout.write(self.style.SUCCESS(('Video Image Captured %s', str(count))))
