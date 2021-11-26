# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(GoalCriteria)
admin.site.register(GoalDescription)
admin.site.register(GoalKRA)
admin.site.register(ActualKeyDelivery)
admin.site.register(Comments)
