# backend/api/serializers.py

from .models import MyModel
from rest_framework import serializers
from .models import NCAABBGame, MLBGame, NFLGame, NCAAFBGame, NBAGame, WNBAGame, MLSGame

class NCAABBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAABBGame
        fields = '__all__'

class MLBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBGame
        fields = '__all__'

class NFLGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLGame
        fields = '__all__'

class NCAAFBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAAFBGame
        fields = '__all__'

class NBAGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAGame
        fields = '__all__'

class WNBAGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = WNBAGame
        fields = '__all__'

class MLSGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLSGame
        fields = '__all__'


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'