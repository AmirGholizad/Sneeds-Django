import random
import string

from rest_framework import generics, mixins, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Discount, Cafe, UserDiscount
from .serializers import CafeSerializer, DiscountSerializer, UserDiscountSerializer


class CafeList(APIView):
    def get(self, request):
        all_cafes = Cafe.objects.all()
        serialize_cafe = CafeSerializer(all_cafes, many=True, context={'request': request})
        return Response(serialize_cafe.data)


class DiscountList(APIView):
    serializer_class = DiscountSerializer

    def post(self, request):
        discount_serializer = DiscountSerializer(data=request.data)
        if discount_serializer.is_valid():
            discount_serializer.save()
            return Response(discount_serializer.data)
        else:
            return Response(discount_serializer.errors)


class UserDiscountList(mixins.CreateModelMixin,
                       generics.ListAPIView):
    serializer_class = UserDiscountSerializer
    passed_id = None

    def get_queryset(self):
        return UserDiscount.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CafePage(APIView):
    def get(self, request, cafe_slug):
        cafe = Cafe.objects.get(slug__exact=cafe_slug)
        cafe_serialize = CafeSerializer(cafe, context={'request': request})
        return Response(cafe_serialize.data)
