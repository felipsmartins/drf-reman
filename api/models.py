# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuidlib

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Customer(models.Model):
    """Uma empresa/cliente/usuário em geral"""
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuidlib.uuid4)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Release(models.Model):
    """Informação de um release/build da aplicação.
    Isso toma como inspiração o "Semantic Versioning" (https://semver.org).

    """
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuidlib.uuid4)
    version = models.CharField(max_length=20)
    codename = models.CharField(max_length=30, blank=True)
    release_date = models.DateTimeField('release_date', default=timezone.now)

    class Meta:
        ordering = ("-release_date",)
        verbose_name_plural = "releases"

    def __str__(self):
        return "v{}".format(self.version)


@python_2_unicode_compatible
class AppPublishing(models.Model):
    """Disponibilização release para usuários."""
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuidlib.uuid4)
    customer = models.ForeignKey(Customer)
    release = models.ForeignKey(Release)
    # data em que a versão foi disponibilizada para o usuário.
    pub_date = models.DateTimeField('pub_date', default=timezone.now)

    def __str__(self):
        return "{} - {}".format(self.customer, self.release)
