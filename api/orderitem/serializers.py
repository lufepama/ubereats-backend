from api.order.models import Order
from api.dish.models import Dish
from rest_framework import serializers
from .models import OrderItem


class OrderItemSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        return instance.get_dish_info


class AddOrderItemSerializer(serializers.Serializer):

    dish = serializers.CharField(max_length=20)
    order = serializers.CharField(max_length=20)
    
    def validate_product(self, value):
        query = Dish.objects.filter(id=int(value))
        if query:
            order_query = Order.objects.get(id=int(self.context['order']))
            dish_query = OrderItem.objects.filter(
                dish=query.first(), order=order_query)
            if not dish_query:
                return value
        return serializers.ValidationError({'error': 'El id no corresponde con nigun plato'})
                                                       
    def create(self, validated_data):
        dish_id = validated_data['dish']
        order_id = validated_data['order']
        dish = Dish.objects.get(id=int(dish_id))
        order = Order.objects.get(id=int(order_id))

        query = OrderItem(dish=dish, order=order)
        query.save()

        return query
