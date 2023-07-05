# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, UserManager

USER_TYPE = (
    ('0', 'CUSTOMER'),
    ('1', 'BUSINESS'),
)


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, auto_created=True)
    user_type = models.IntegerField(choices=USER_TYPE)

    class Meta:
        app_label = 'detty_server'


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, auto_created=True)
    location = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    event_description = models.CharField(max_length=255)
    event_summary = models.CharField(max_length=255)

    class Meta:
        app_label = 'detty_server'


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, auto_created=True)
    user_id = User.user_id
    event_id = Event.event_id
    comment = models.CharField(max_length=255)

    class Meta:
        app_label = 'detty_server'
