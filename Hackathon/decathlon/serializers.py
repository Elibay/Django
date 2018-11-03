from rest_framework import serializers
from .models import *

# admin.site.register(Customer)
# admin.site.register(Marathon)
# admin.site.register(Club)
# admin.site.register(Product)
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MarathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marathon
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
