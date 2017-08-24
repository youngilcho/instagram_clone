# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from utils import FilePathManager


class InstagramUser(models.Model):
    """
        사용자 계정과 관련된 정보를 저장하는 모델
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    profile_image = models.ImageField(upload_to=FilePathManager('account/instagram_user/profile/image/'))


class UserRelationship(models.Model):
    """
        사용자 간 팔로잉 관계를 저장하는 모델
    """
    user = models.ForeignKey(InstagramUser, related_name='relation_user')
    follower = models.ForeignKey(User, related_name='relation_follower')

    created_at = models.DateTimeField(auto_now_add=True)
