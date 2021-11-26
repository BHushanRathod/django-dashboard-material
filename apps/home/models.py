# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class GoalCriteria(models.Model):
    name = models.TextField(blank=False)
    weightage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class GoalDescription(models.Model):
    criteria = models.ForeignKey(GoalCriteria, on_delete=models.CASCADE)
    description = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.criteria.name}-{self.description}"


class GoalKRA(models.Model):
    goal_description = models.ForeignKey(GoalDescription, on_delete=models.CASCADE)
    description = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.description}"


class ActualKeyDelivery(models.Model):
    goal_kra = models.ForeignKey(GoalKRA, on_delete=models.CASCADE)
    description = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.description}"


class Comments(models.Model):
    delivery = models.ForeignKey(ActualKeyDelivery, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.comment}"

