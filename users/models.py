from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()


# Profile Model
class Profile(models.Model):
    """We import a user from django, we set the method One to One"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="catalog_pics/default.jpg", upload_to='catalog_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Function for photo processing
    def save(self, **kwargs):
        super().save(**kwargs)
        img = Image.open(self.image.path)
        if img.height > 150 or img.width > 150:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)









