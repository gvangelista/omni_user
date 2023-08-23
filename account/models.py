from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin


from django.utils.translation import gettext_lazy as _

# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
        verbose_name=_('Id')
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name=_('Created at')
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        verbose_name=_('Modified at')
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name=_('Active'),
    )

    class Meta:
        abstract = True
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(
        db_column='tx_username',
        null=False,
        max_length=64,
        unique=True
    )

    password = models.CharField(
        db_column='tx_password',
        null=False,
        max_length=104,
    )
    name = models.CharField(
        db_column='tx_name',
        null=True,
        max_length=256
    )

    email = models.CharField(
        db_column='tx_email',
        null=True,
        max_length=256
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'user'





