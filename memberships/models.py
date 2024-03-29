from django.db import models

from django.conf import settings
from cannabis_db.models import Strain
# Create your models here.
from ckeditor.fields import RichTextField

from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):
          user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
          biography = RichTextField(max_length=10000, null=True, blank=True)


          profile_photo = ThumbnailerImageField(default='/MEMBERSHIP/PROFILE_PHOTOS/default_profile_photo.png', upload_to='PROFILE_PHOTOS')

          website_url = models.URLField(max_length=1000,null=True, blank=True)
          twitter = models.URLField(max_length=1000,null=True, blank=True)
          facebook = models.URLField(max_length=1000,null=True, blank=True)
          youtube = models.URLField(max_length=1000,null=True, blank=True)
          instagram = models.URLField(max_length=1000,null=True, blank=True)




          saved_strains = models.ManyToManyField(Strain,null=True, blank=True)

          followers = models.ManyToManyField('self',null=True, blank=True)

          def __str__(self):
                    return str(self.user)