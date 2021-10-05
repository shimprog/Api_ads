from rest_framework import generics, filters
from mainapp.models import Advert
from mainapp.serializers import AdvertSerializer, AdvertListSerializer


class AdvertList(generics.ListCreateAPIView):
    # поля в ответе: название объявления, ссылка на главное фото (первое в списке), цена
    queryset = Advert.objects.all()
    serializer_class = AdvertListSerializer
    filter_backends = [filters.OrderingFilter]
    # нужна возможность сортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание)
    ordering_fields = ['price', 'date']


class AdvertCreate(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    filter_backends = [filters.OrderingFilter]
    # нужна возможность сортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание)
    ordering_fields = ['price', 'date']


class AdvertDetail(generics.RetrieveUpdateDestroyAPIView):
    # обязательные поля в ответе: название объявления, цена, ссылка на главное фото
    queryset = Advert.objects.all()
    serializer_class = AdvertListSerializer


class AdvertDetailFull(generics.RetrieveUpdateDestroyAPIView):
    # опциональные поля (можно запросить, передав параметр fields): описание, ссылки на все фото
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer



