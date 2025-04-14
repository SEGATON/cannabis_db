from django.db import models

from django.conf import settings
from cannabis_db.models import Strain, Dispensary
# Create your models here.
from ckeditor.fields import RichTextField

from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
  biography = RichTextField(max_length=10000, null=True, blank=True)


  profile_photo = models.ImageField(default='/MEMBERSHIP/PROFILE_PHOTOS/default_profile_photo.png', upload_to='PROFILE_PHOTOS')

  website_url = models.URLField(max_length=1000,null=True, blank=True)
  twitter = models.URLField(max_length=1000,null=True, blank=True)
  facebook = models.URLField(max_length=1000,null=True, blank=True)
  youtube = models.URLField(max_length=1000,null=True, blank=True)
  instagram = models.URLField(max_length=1000,null=True, blank=True)


  bookmarks = models.ManyToManyField('cannabis_db.Strain', null=True, blank=True, related_name='bookmarked_strains')

  saved_strains = models.ManyToManyField(Strain,null=True, blank=True)

  saved_dispensaries = models.ManyToManyField(Dispensary,null=True, blank=True)

  followers = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='profile_follower')


  verified = models.BooleanField(default=False)


  address = models.ForeignKey('addresses.Address', on_delete=models.CASCADE,null=True, blank=True)


  date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
  date_updated = models.DateTimeField(null=True,blank=True)
  date_deleted = models.DateTimeField(null=True,blank=True)

  VISIBILTY_OPTIONS = (
  ('public','Public',),
  ('private','Private',),
  )

  visibility_options = models.CharField(max_length=50, choices=VISIBILTY_OPTIONS,null=True, blank=True, default='public' )

  def __str__(self):
    return str(self.user)