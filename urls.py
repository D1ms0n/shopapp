
'''studio URL Configuration

The  list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
'''
from django.conf.urls import include,url

from django.conf import settings


from django.contrib.auth import views as auth_views

from shopapp import views as app_views
from shopapp.views import api_views as api_views

urlpatterns = [

    url(r'^$',           app_views.main, name='home'),
    url(r'^home/$',      app_views.main, name='home'),
    url(r'^instashop/$', app_views.main, name='home'),
    url(r'^basket/$',    app_views.main, name='home'),

    url(r'^insta_shop/$', app_views.insta_shop, name='insta_shop'),
    url(r'^api_test/$',   app_views.api_test,   name='api_test'),

    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='studio/login.html',redirect_field_name ='/admin/') , name='login'),

    # REST API

    url(r'^api/medias/$',                             api_views.InstaMediaList.as_view(),      name='medias'),
    url(r'^api/shop_items/$',                         api_views.InstaShopItemList.as_view(),   name='shop_items'),

    url(r'^api/orders/$',                             api_views.OrderList.as_view(),           name='orders'),
    url(r'^api/orders/(?P<id>[0-9]+)/$',              api_views.OrderDetail.as_view(),         name='order'),

     #url(r'^api/order_items/$',                        app_views.OrderItemList.as_view(),   name='order_items'),


]
