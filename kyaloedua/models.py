from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RoomPost(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    subtopic = models.CharField(max_length=255, null=True,  blank=True)
    body = RichTextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:   
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomPost, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:   
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

