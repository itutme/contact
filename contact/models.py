from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    phone_mobile = models.CharField(max_length=30)
    phone_work = models.CharField(max_length=30, blank=True)
    phone_home = models.CharField(max_length=30, blank=True)
    profile_photo = models.ImageField(upload_to='photo/%Y/%m', blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=2, blank=True)
    postal_zip = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    ip = models.TextField(
        blank=True, verbose_name=_('Instant Messenger'),
        help_text=_('e.g. Skype: johndoe'))
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
