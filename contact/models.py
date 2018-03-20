# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField(max_length=500)