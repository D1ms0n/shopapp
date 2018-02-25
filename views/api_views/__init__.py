from rest_framework import generics
from rest_framework import pagination
from shopapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework import status

from shopapp.serializers import *

from rest_framework.renderers import JSONRenderer

from logger import Logger
from django_datastore import *

logger = Logger('API_VIEW')



class InstaMediaList(generics.ListCreateAPIView):
    serializer_class = InstaMediaSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        return InstaMedia.objects.all()

class InstaShopItemList(generics.ListCreateAPIView):
    serializer_class = InstaShopItemSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):

        category = self.request.query_params.get('category')

        if category:
            items = InstaShopItem.objects.filter(category = category)
        else:
            items = InstaShopItem.objects.all()

        return items


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Order.objects.all()

    def create(self, request, *args, **kwargs):
        items = request.data.pop('items')

        order = Order(**request.data)
        order.save()

        for item in items:
            shop_item =  InstaShopItem.objects.get(id = item['id'])
            OrderItem.objects.create(shop_item = shop_item,
                                     order = order,
                                     count = item['count'])

        serializer = self.get_serializer(order)

        return Response(serializer.data)


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = (JSONRenderer,)
    lookup_field = 'id'
