from rest_framework import serializers
from .models import custumer

class custumerserializer(serializers.ModelSerializer):
    
    class Meta:

        model = custumer
        fields = '__all__'
