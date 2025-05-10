from rest_framework import serializers
from .models import NewsThree

class NewsThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsThree
        fields = ['id', 'title', 'description', 'image']