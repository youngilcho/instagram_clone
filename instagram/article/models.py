# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

from account.models import InstagramUser

@deconstructible
class FilePathManager(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def _gen_filename_hash(self):
        import uuid
        return str(uuid.uuid4())

    def __call__(self, instance, filename):
        import time
        import datetime
        import os
        name, extend = os.path.splitext(filename)
        name = self._gen_filename_hash()
        filename = "%s%s" % (name, extend)
        return self.path + str(datetime.datetime.now().strftime("%Y%m%d")) + "/" + filename


class Article(models.Model):
    user = models.ForeignKey(InstagramUser)
    photo = models.ImageField(pload_to=FilePathManager('article/'))
    text = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(InstagramUser)

    created_at = models.DateTimeField(auto_now_add=True)
