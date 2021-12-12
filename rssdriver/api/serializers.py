from ..models import Article, Channel
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('users',)


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        exclude = ('users', 'status')


class ChannelFollowSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all())

    class Meta:
        model = Channel
        fields = ['id']


class ArticleFollowSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = Channel
        fields = ['id']
