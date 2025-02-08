from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# from school.models import Teacher
# from .models import User
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "profile/%s.%s"%(instance.id,extension)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'administrator'),
        ('teacher', 'teacher'),
        ('student', 'student'),
        ('staff', 'staff'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    b_date = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True,null=True)
    image = models.ImageField(upload_to=image_upload, verbose_name="profile Image", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            
            # Resize Image (Optional)
            max_size = (800, 800)  # Set max width & height
            img.thumbnail(max_size)  # Maintain Aspect Ratio

            # Compress Image
            img_io = BytesIO()
            img.save(img_io, format='JPEG', quality=60)  # Adjust quality (lower = more compression)
            self.image = ContentFile(img_io.getvalue(), name=self.image.name)

        super().save(*args, **kwargs)


