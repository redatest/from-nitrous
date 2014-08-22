from django.conf import settings
from car_shop.models import Offer
from django.utils.translation import ugettext_lazy as _

def strings(request):
	""" context processor for the site templates """
	if request.LANGUAGE_CODE == "en":
		direction = "ltr"
	else:
		direction = "rtl"
	
	direction =  "ltr"
	return {
			'request': request,
			'direction' : direction

			}

