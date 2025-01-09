from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.timezone import now

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/' , blank=True, null=True)
    nickname = models.CharField(max_length=15 , unique=True, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(blank=True , null=True)
    bio = models.TextField(blank=True, null=True)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress' , 'In Progress'),
        ('completed' , 'Completed'),
        ('expired', 'Expired'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    deadline = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, default='in_progress', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def mark_expired(self):
        if self.deadline < now() and self.status == 'in_progress':
            self.status = 'expired'
            self.save()
        
        def __str__(self):
            return self.title