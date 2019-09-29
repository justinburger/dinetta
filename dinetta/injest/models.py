from django.db import models

class CameraGroup(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.label)

class Camera(models.Model):
    label = models.CharField(max_length=30)
    connection_string = models.TextField()
    camera_group = models.ForeignKey(CameraGroup, on_delete=models.CASCADE)

    def __str__(self):
        return '%s > %s' % (self.camera_group.label, self.label)
