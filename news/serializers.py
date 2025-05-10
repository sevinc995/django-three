from rest_framework import serializers
from .models import NewsThree

class NewsThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsThree
        field = ['id', 'title', 'description', 'image']