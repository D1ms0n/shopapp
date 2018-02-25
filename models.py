# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
 # ----------------------------------------- INSTA ---------------------------------------------------


class InstaUserCred(models.Model):
    class Meta(object):
        verbose_name = u"InstaUserCred"
        verbose_name_plural = u"InstaUsersCreds"
    def __unicode__(self):
        return u"%s..." % (self.user_login)

    user_login           = models.CharField(max_length=256, blank=True, verbose_name=u"Login", primary_key=True)
    user_pass            = models.CharField(max_length=256, blank=False, verbose_name=u"Password", null= True)
    user                 = models.ForeignKey(User, related_name='creds', on_delete=models.CASCADE)




class Insta_tag(models.Model):
    class Meta(object):
        verbose_name = u"Tag"
        verbose_name_plural = u"Tags"
    def __unicode__(self):
        #self.content_part=self.tag_title[0:100]
        return u"%s..." % (self.tag_title)

    tag_id           = models.CharField(max_length=256, blank=False, verbose_name=u"Id")
    tag_title        = models.CharField(max_length=256,   blank=False, verbose_name=u"Title")
    tag_images_count = models.IntegerField(blank=True,verbose_name=u"Image count")

class InstaUser(models.Model):
    class Meta(object):
        verbose_name = u"InstaUser"
        verbose_name_plural = u"InstaUser"
    def __unicode__(self):
        return u"%s..." % (self.user_name)

    user_id              = models.CharField(max_length=256, blank=True, verbose_name=u"Id", primary_key=True)
    user_name            = models.CharField(max_length=256, blank=False, verbose_name=u"User_login", null= True)
    user_full_name       = models.CharField(max_length=256, verbose_name=u"User_full_name",null= True)
    followers_count      = models.IntegerField(             blank=True, null= True)
    follow_count         = models.IntegerField(             blank=True, null= True)
    profile_pic_url_hd   = models.CharField(max_length=256, blank=True, null= True)
    user_biography       = models.CharField(max_length=256, blank=True, null= True)
    user_external_url    = models.CharField(max_length=256, blank=True, null= True)
    follows_viewer       = models.CharField(max_length=256, blank=True, null= True)
    followed_by_viewer   = models.CharField(max_length=256, blank=True, null= True)            # followed, followed_by_bot, unfollowed_by_bot,  in_order_to_follow, in_order_to_unfollow
    has_requested_viewer = models.CharField(max_length=256, blank=True, null= True)
    requested_by_viewer  = models.CharField(max_length=256, blank=True, null= True)            # requested_by_viewer, requested_by_bot
    has_blocked_viewer   = models.CharField(max_length=256, blank=True, null= True)
    blocked_by_viewer    = models.CharField(max_length=256, blank=True, null= True)
    is_private           = models.CharField(max_length=256, blank=True, null= True)


class InstaBotTask(models.Model):
    class Meta(object):
        verbose_name = u"Task"
        verbose_name_plural = u"Tasks"
    def __unicode__(self):
        return u"%s" % (self.task_id)

    task_id     = models.CharField(max_length = 256, blank = True,  verbose_name = u"Task id", primary_key = True)
    operation   = models.CharField(max_length = 256, blank = False, verbose_name = u"Operation", null = True)
    username    = models.CharField(max_length = 256, blank = True, verbose_name=u"User_login", null= True)
    status      = models.CharField(max_length = 256, blank = True, verbose_name=u"Status", null= True)
    create_time = models.CharField(max_length = 256, blank = True, verbose_name=u"Create time", null= True)
    count       = models.CharField(max_length = 256, blank = True, verbose_name=u"Count", null= True)
    #args        = models.CharField(max_length = 256, blank = False, verbose_name=u"Args", null= True)

class Task_to_user_map(models.Model):
    class Meta(object):
        verbose_name = u"Task_to_user_map"
        verbose_name_plural = u"Task_to_user_maps"
    def __unicode__(self):
        return u"%s" % (self.task_id)

    map_id =  models.AutoField(primary_key=True)
    task_id = models.ForeignKey(InstaBotTask, on_delete = models.CASCADE)
    user_id = models.ForeignKey(InstaUser,     on_delete = models.CASCADE,  null= True)
    #user_name = models.CharField(max_length=256, blank=False, verbose_name=u"User_login", null= True)



class TaskTarget(models.Model):
    class Meta(object):
        verbose_name = u"Task_to_arg_map"
        verbose_name_plural = u"Task_to_arg_maps"
    def __unicode__(self):
        return u"%s" % (self.task_id)

    map_id    =  models.AutoField(primary_key=True)
    task      = models.ForeignKey(InstaBotTask, related_name='targets', on_delete = models.CASCADE)
    user_name = models.CharField(max_length=256, blank=True, verbose_name=u"User_name", null= True)
    tag_name  = models.CharField(max_length=256, blank=True, verbose_name=u"Tag_name",  null=True)
    photo_id  = models.CharField(max_length=256, blank=True, verbose_name=u"Photo_id",  null=True)

class Relationship(models.Model):
    class Meta(object):
        verbose_name = u"Relationship"
        verbose_name_plural = u"Relationships"
    def __unicode__(self):
        return u"%s..." % (self.rel_id)

    rel_id           = models.AutoField(primary_key=True)
    followed_user_id = models.CharField(max_length=256, blank=False, verbose_name=u"Followed user id", null= True)
    user_id          = models.CharField(max_length=256, blank=False, verbose_name=u"User id", null= True)
    #kind             = models.CharField(max_length=256, blank=False, verbose_name=u"Relation kind", null= True)



class InstaMedia(models.Model):
    class Meta(object):
        verbose_name = u"Media"
        verbose_name_plural = u"Medias"
    def __unicode__(self):
        #self.content_part=self.image_id[0:100]
        return u"%s..." % (self.image_id)

    image_id           = models.CharField(max_length=256, blank=False, verbose_name=u"Id")
    caption            = models.TextField(blank=True, verbose_name=u"Caption")
    image_author       = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    likes_count        = models.CharField(max_length=256, blank=True, verbose_name=u"Likes count")
    code               = models.CharField(max_length=256, blank=True, verbose_name=u"Code")

class InstaMediaSRC(models.Model):
    class Meta(object):
        verbose_name = u"Media src"
        verbose_name_plural = u"Media srcs"
    def __unicode__(self):
        #self.content_part=self.image_id[0:100]
        return u"%s..." % (self.media_src)

    media_src           = models.CharField(max_length=256, blank=False, verbose_name=u"SRC")
    insta_media         = models.ForeignKey(InstaMedia, related_name='srcs', on_delete=models.CASCADE)




    #images_tags =  models.ManyToManyField(Insta_tag)

class InstaShopItem(models.Model):
    class Meta(object):
        verbose_name = u"Shop item"
        verbose_name_plural = u"Shop items"
    def __unicode__(self):
        #self.content_part=self.image_id[0:100]
        return u"%s..." % (self.media)

    id          = models.AutoField(primary_key=True, verbose_name=u"Id")
    name        = models.CharField(max_length=256, blank=True, verbose_name=u"Name")
    media       = models.ForeignKey(InstaMedia, on_delete=models.CASCADE)
    price       = models.CharField(max_length=256, blank=False, verbose_name=u"Price")
    category    = models.CharField(max_length=256, blank=True, verbose_name=u"Category")
    description = models.TextField(blank=True, verbose_name=u"Description")



class Order(models.Model):
    class Meta(object):
        verbose_name = u"Order"
        verbose_name_plural = u"Orders"
    def __unicode__(self):
        #self.content_part=self.image_id[0:100]
        return u"%s..." % (self.id)

    id      = models.AutoField(primary_key=True)
    #media   = models.ForeignKey(InstaMedia, on_delete=models.CASCADE)
    name    = models.CharField(max_length=256, blank=False, verbose_name=u"Name")
    mail    = models.CharField(max_length=256, blank=False, verbose_name=u"Mail")
    phone   = models.CharField(max_length=256, blank=False, verbose_name=u"Phone")
    address = models.CharField(max_length=256, blank=False, verbose_name=u"Address")
    comment = models.TextField(blank=True, verbose_name=u"Description")

class OrderItem(models.Model):
    class Meta(object):
        verbose_name = u"Order Item"
        verbose_name_plural = u"Order Items"
    def __unicode__(self):
        #self.content_part=self.image_id[0:100]
        return u"%s..." % (self.id)

    #media   = models.ForeignKey(InstaMedia, on_delete=models.CASCADE)
    order     = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    shop_item = models.ForeignKey(InstaShopItem, related_name='items', on_delete=models.CASCADE)
    count     = models.CharField(max_length=256, blank=False, verbose_name=u"Count")
    

    

    