from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.avatar.path) # Open image
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.avatar.path) # Save it again and override the larger image