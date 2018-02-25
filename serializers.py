import time

from rest_framework import serializers
from shopapp.models import *
from django.contrib.auth.models import User

from logger import Logger
logger = Logger('view')

class CredSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUserCred
        fields = ('user_login',
                  'user_pass')



class UserSerializer(serializers.ModelSerializer):
    creds = CredSerializer(required = False)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password',
                  'creds')

    def create(self, validated_data):
        cred_data = validated_data.pop('creds')
        print cred_data['user_login']

        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        cred = InstaUserCred(user_login = cred_data['user_login'],
                             user_pass  = cred_data['user_pass'],
                             user = user)

        cred.save()
        return user


class InstaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = ('user_id',
                  'user_name',
                  'user_full_name',
                  'followers_count',
                  'follow_count',
                  'profile_pic_url_hd',
                  'user_biography',
                  'user_external_url',
                  'follows_viewer',
                  'followed_by_viewer',
                  'has_requested_viewer',
                  'requested_by_viewer',
                  'has_blocked_viewer',
                  'blocked_by_viewer',
                  'is_private')

class _short_InstaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = ('user_id',
                  'user_name',
                  'profile_pic_url_hd')





class InstaMediaSRCSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaMediaSRC
        fields = ('media_src',)

class InstaMediaSerializer(serializers.ModelSerializer):
    image_author = _short_InstaUserSerializer()
    srcs         = InstaMediaSRCSerializer(many = True)

    class Meta:
        model = InstaMedia
        fields = ('image_id',
                  'srcs',
                  'caption',
                  'image_author',
                  'likes_count',
                  'code')


class _short_InstaMediaSerializer(serializers.ModelSerializer):
    srcs         = InstaMediaSRCSerializer(many = True)

    class Meta:
        model = InstaMedia
        fields = ('srcs',
                  'likes_count')

class InstaShopItemSerializer(serializers.ModelSerializer):
    media = _short_InstaMediaSerializer()

    class Meta:
        model = InstaShopItem
        fields = ('id',
                  'name',
                  'media',
                  'price',
                  'description',
                  'category')

class _OrderItemSerializer(serializers.ModelSerializer):
    shop_item = InstaShopItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('shop_item',
                  'count')



class OrderSerializer(serializers.ModelSerializer):
    items =_OrderItemSerializer(many = True, required = False)
    class Meta:
        model = Order
        fields = ('id',
                  'name',
                  'mail',
                  'phone',
                  'address',
                  'comment',
                  'items')
