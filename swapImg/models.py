from django.db import models

class UserInfo(models.Model):
    userName = models.CharField(max_length=50)
    userAvatar = models.ImageField(upload_to='images/')
    userAnimeAvatar = models.ImageField(upload_to='images/')

def __str__(self):
     return self.title