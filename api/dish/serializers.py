from rest_framework import serializers


class DishSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):

        return {
            'name':instance.name,
            'description':instance.description,
            'price':instance.price,
            'previousPrice':instance.previous_price,
            'image':instance.imageURL,
            'rating':instance.rating,
            'id':instance.id
        }