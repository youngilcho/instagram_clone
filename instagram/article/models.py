# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

from account.models import InstagramUser

from utils import FilePathManager


class Article(models.Model):
    """
        게시글 정보를 저장하는 모델
    """
    user = models.ForeignKey(InstagramUser)
    photo = models.ImageField(pload_to=FilePathManager('article/article/photo/'))
    text = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
        댓글 정보를 저장하는 모델
    """
    article = models.ForeignKey(Article)
    user = models.ForeignKey(InstagramUser)
    comment = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    """
        Like 정보를 저장하는 모델
    """
    article = models.ForeignKey(Article)
    user = models.ForeignKey(InstagramUser)

    created_at = models.DateTimeField(auto_now_add=True)
