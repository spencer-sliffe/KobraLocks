# backend/api/serializers.py

from rest_framework import serializers
from .models import MyModel
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'