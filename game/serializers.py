from rest_framework import serializers
from users.serializers import CustomUserSerializer
from .models import Team, Player, Category, CategoryData, Result, GuessedAnswer


class TeamSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Team
        fields = ['id', 'user', 'name']



class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Player
        fields = ['__all__']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryDataSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryData
        fields = ['__all__']


class ResultSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Result
        fields = ['__all__']


class GuessedAnswerSerializer(serializers.ModelSerializer):
    guessed_by = PlayerSerializer()
    guessed_answer = CategoryDataSerializer()

    class Meta:
        model = GuessedAnswer
        fields = ['__all__']
