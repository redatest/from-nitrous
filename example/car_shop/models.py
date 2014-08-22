from django.db import models
from car_shop.fields import ThumbnailImageField 
from model_choices import REGION_CHOICES, SALARY_CHOICES, CATEGORY_CHOICES, OFFER_CHOICES, YESNO
import datetime
import math
from managers import OfferManager, OfferQuerySets

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class Offer(models.Model):
	""" Job offers model """
	user 		= models.ForeignKey(User)

	title 		= models.CharField(max_length=250)
	offerType 	= models.CharField(max_length = 200, choices=OFFER_CHOICES, default='1')
	category 	= models.CharField(max_length = 200, choices=CATEGORY_CHOICES, default='1')
	region 		= models.IntegerField(choices=REGION_CHOICES)
	salary 		= models.IntegerField(blank=True, choices=SALARY_CHOICES)

	views 		= models.IntegerField(_('Views count'), blank=True, default=0)
	description = models.TextField(_('description'), blank=True, null=True)

	created 	= models.DateTimeField(_('Created'), null=True)
	modified 	= models.DateTimeField(_('Modified'), null=True)
	immediate 	= models.CharField(max_length = 20, choices=YESNO, default='1')
	# sold 		= models.BooleanField(_('Sold'), blank=True, default=False)

	activated 	= models.BooleanField(_('Activated'), blank=True, default=True)
	image 		  = ThumbnailImageField(upload_to = 'img/' ,  help_text = "for better resolution image size must be 600x280")
	
	def __unicode__(self):
		return unicode(OFFER_CHOICES[int(self.offerType)][1])

	def region_display(self):	
		# return self.region
		return REGION_CHOICES[int(self.region)][1]

	def salary_display(self):
		return self.salary

	def category_display(self):
		return CATEGORY_CHOICES[int(self.category)][1]

	def offerType_display(self):
		return OFFER_CHOICES[int(self.offerType)][1]	

	def get_absolute_url(self):
		return '/offer/%s' %(self.id)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created = datetime.datetime.today()
		self.modified = datetime.datetime.today()
		return super(Offer, self).save(*args, **kwargs)	
	
	def delete(self, *args, **kwargs):
		print 'deleting 2'
		# You have to prepare what you need before delete the model
		storage, path, marked_path, thumb_path, big_marked_path = self.image.storage, self.image.path, self.image.marked_path, self.image.thumb_path, self.image.big_marked_path
		# Delete the model before the file
		super(Offer, self).delete(*args, **kwargs)

		# Delete all associated files after the model
		storage.delete(path)
		storage.delete(marked_path)
		storage.delete(thumb_path)
		storage.delete(big_marked_path)

	# this a function for the image list display
	def image_tag(self):

		return u'<img src="%s" width="80" height="80" />' % self.image.url
		image_tag.short_description = 'Image'

	image_tag.allow_tags = True	

	objects = OfferManager()


# to be comment on the first sb sync
# class UserUploadedCars(Car):
# 	class Meta:
# 		proxy = True

# 		verbose_name_plural = "Cars uploaded by users"


class Setting(models.Model):
	key = models.CharField(max_length=32)
	value = models.CharField(max_length=200)
	def __unicode__(self):
		return self.key


class Article(models.Model):

	title = models.CharField(blank=True, max_length=50)
	summary = models.TextField()
	body = models.TextField()
	created = models.DateTimeField(default=datetime.datetime.now)
	is_watermarked = models.BooleanField(default=False)
	img = ThumbnailImageField(upload_to='photos', blank=True, help_text = "for better resolution image size must be 600x280")
	image_title = models.CharField(max_length=200, blank=True, null=True)

	class Meta:
		ordering = ['created']
		verbose_name_plural = "articles"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/news_item/%s' % self.id

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    adress = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)

# automatically create a userinfo realted to the new registerd user
@receiver(post_save, sender=User)
def create_info_user(sender,instance, signal, created, **kwargs):
    print "#####  a new user is created  ######"
    if created:
        UserInfo(user = instance).save()
