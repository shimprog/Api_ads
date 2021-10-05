from rest_framework import pagination, serializers
from mainapp.models import Advert


class PageNumberPaginationWithCount(pagination.PageNumberPagination):
    # нужна пагинация, на одной странице должно присутствовать 10 объявлений
    def get_paginated_response(self, data):
        response = super(PageNumberPaginationWithCount, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class AdvertListSerializer(serializers.ModelSerializer):
    # поля в ответе: название объявления, ссылка на главное фото (первое в списке), цена
    class Meta:
        model = Advert
        fields = ['title', 'img', 'price']


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'img', 'additional_img', 'additional_img_2', 'price']

    def create(self, validated_data):
        return Advert.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.img = validated_data.get('img', instance.img)
        instance.additional_img = validated_data.get('additional_img', instance.additional_img)
        instance.additional_img_2 = validated_data.get('additional_img_2', instance.additional_img_2)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        return instance
