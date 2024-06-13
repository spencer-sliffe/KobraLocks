# backend/api/serializers.py

from .models import MyModel
from rest_framework import serializers
from .models import NCAABBGame, MLBGame, NFLGame, NCAAFBGame, NBAGame, WNBAGame, MLSGame, MLBFutures, MLBSpecials, MLBPlayerFutures, MLBTeamPlayoffs, MLBWinTotals, NFLDivisionSpecials, NFLFutures, NFLPlayerFutures, NFLPlayerTotals, NFLSeasonSpecials, NBAFutures, NBAPlayerFutures, NCAABBFutures, MLSFutures, WNBAFutures, WNBAPlayerFutures

# NCAABB
class NCAABBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAABBGame
        fields = '__all__'

class NCAABBFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAABBFutures
        fields = '__all__'

# MLB
class MLBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBGame
        fields = '__all__'

class MLBFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBFutures
        fields = '__all__'

class MLBSpecialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBSpecials
        fields = '__all__'

class MLBPlayerFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBPlayerFutures
        fields = '__all__'

class MLBTeamPlayoffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBTeamPlayoffs
        fields = '__all__'

class MLBWinTotalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBWinTotals
        fields = '__all__'

# NFL
class NFLGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLGame
        fields = '__all__'

class NFLFutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLFutures
        fields = '__all__'

class NFLPlayerFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLPlayerFutures
        fields = '__all__'

class NFLPlayerTotalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLPlayerTotals
        fields = '__all__'

class NFLDivisionSpecialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLDivisionSpecials
        fields = '__all__'

class NFLSeasonSpecialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLSeasonSpecials
        fields = '__all__'

# NCAAFB
class NCAAFBGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAAFBGame
        fields = '__all__'

# NBA
class NBAGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAGame
        fields = '__all__'

class NBAFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAFutures
        fields = '__all__'

class NBAPlayerFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAPlayerFutures
        fields = '__all__'

# WNBA
class WNBAGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = WNBAGame
        fields = '__all__'

class WNBAFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WNBAFutures
        fields = '__all__'

class WNBAPlayerFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WNBAPlayerFutures
        fields = '__all__'

#MLS
class MLSGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLSGame
        fields = '__all__'

class MLSFuturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLSFutures
        fields = '__all__'

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'