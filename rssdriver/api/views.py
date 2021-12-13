from django.utils.translation import gettext as _
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from feeder.pagination import PaginationHandlerMixin, BasicPagination


class ChannelView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        return Response({
            'success': True,
            'data': self.get_paginated_response(
                ChannelSerializer(self.paginate_queryset(Channel.objects.filter(is_disable=False).all()),
                                  many=True).data).data,
            'message': _('show all Channel'),
            'dev_message': 'show all Channel'

        })


class ArticleView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk):
        return Response({
            'success': True,
            'data': self.get_paginated_response(
                ArticleSerializer(self.paginate_queryset(Article.objects.filter(channel_id=pk).all()),
                                  many=True).data).data,
            'message': _('welcome to Digi_Cloud'),
            'dev_message': 'token generate'

        })


class ChannelFollowView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        return Response({
            'success': True,
            'data': self.get_paginated_response(
                ChannelSerializer(
                    self.paginate_queryset(Channel.objects.filter(users=request.user, is_disable=False).all()),
                    many=True).data).data,
            'message': _('show follow Channel'),
            'dev_message': 'show follow Channel'

        })

    def post(self, request):
        serializer = ChannelFollowSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, 'dev_message': 'wrong id'
                                , "message": _('your information is not correct'),
                             'data': {'messages': serializer.errors}},
                            status=status.HTTP_400_BAD_REQUEST)

        channel = Channel.objects.filter(id=request.data['id']).prefetch_related('users').first()
        channel.toggle_Follow(user=request.user)

        return Response({
            'success': True,
            'message': _('welcome to Digi_Cloud'),
            'dev_message': 'token generate'

        })


class SpecifivChannelArticleFavoriteView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, pk):
        return Response({
            'success': True,
            'data': self.get_paginated_response(
                ArticleSerializer(
                    self.paginate_queryset(Article.objects.filter(users=request.user, channel=pk).all()),
                    many=True).data).data,
            'message': _('show follow Channel'),
            'dev_message': 'show follow Channel'

        })


class ArticleFavoriteView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        return Response({
            'success': True,
            'data': self.get_paginated_response(
                ArticleSerializer(
                    self.paginate_queryset(Article.objects.filter(users=request.user).all()),
                    many=True).data).data,
            'message': _('show follow ArticleFavorite'),
            'dev_message': 'show follow ArticleFavorite'

        })

    def post(self, request):
        serializer = ArticleFollowSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, 'dev_message': 'wrong id'
                                , "message": _('your information is not correct'),
                             'data': {'messages': serializer.errors}},
                            status=status.HTTP_400_BAD_REQUEST)

        article = Article.objects.filter(id=request.data['id']).first()
        article.toggle_favorite(user=request.user)

        return Response({
            'success': True,
            'message': _('welcome to Digi_Cloud'),
            'dev_message': 'token generate'

        })
