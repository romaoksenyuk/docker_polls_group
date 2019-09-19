from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = News
        fields = ('title', 'description', 'news_link', 'image', 'is_checked',)
