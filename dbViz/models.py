# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ColumbiaGISVeg(models.Model):
	treeshrub = models.IntegerField()
	impervious = models.IntegerField()
	lawn = models.IntegerField()
	water = models.IntegerField()
