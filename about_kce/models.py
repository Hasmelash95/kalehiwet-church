from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Profile model for info page.
    """
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    user_name = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    email = models.EmailField()
    image = CloudinaryField('image', default='temporary')
    role = models.CharField(max_length=30, default='Helper')
    about = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.first_name + self.last_name