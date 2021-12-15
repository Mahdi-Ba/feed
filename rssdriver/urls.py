from django.urls import path
from .api import views

urlpatterns = [
    path('channel', views.ChannelView.as_view(), name='ChannelView'),
    path('channel/<int:pk>/article', views.ArticleView.as_view(), name='ArticleView'),
    path('channel/follow', views.ChannelFollowView.as_view(), name='ChannelFollowView'),
    path('channel/<int:pk>/article/favorite', views.SpecifivChannelArticleFavoriteView.as_view(),
         name='SpecifivChannelArticleFavoriteView'),
    path('channel/article/favorite', views.ArticleFavoriteView.as_view(), name='ArticleFavoriteView'),
]

# ChannelView
"""
curl --location --request GET '127.0.0.1:8000/api/v1/rss/channel' \
--header 'Authorization:  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY' \
--data-raw ''
"""


# ArticleView
"""
curl --location --request GET '127.0.0.1:8000/api/v1/rss/channel/1/article' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNzAwMDM2Mjk2LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5NTU2Mjk2fQ.w0oNqIegKDiF0mR9giRx_h91sU1ZiiEJVZ9hpfWoy8w' \
--data-raw ''
"""

# ChannelFollowView

"""
curl --location --request GET '127.0.0.1:8000/api/v1/rss/channel/follow' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY' \
--data-raw ''

"""

"""
curl --location --request POST '127.0.0.1:8000/api/v1/rss/channel/follow' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id":1
}'
"""





# SpecifivChannelArticleFavoriteView


"""
curl --location --request GET '127.0.0.1:8000/api/v1/rss/channel/2/article/favorite' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY'

"""





# ArticleFavoriteView


"""
curl --location --request GET '127.0.0.1:8000/api/v1/rss/channel/article/favorite' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY'
"""


"""
curl --location --request POST '127.0.0.1:8000/api/v1/rss/channel/article/favorite' \
--header 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFhIiwiZXhwIjoxNjk5NzE4MTAxLCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjM5MjM4MTAxfQ.Y3hgNSHIMu49lgpettahhJ6Qjo4cKSkN99vHjPUEYGY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id":1675
}'
"""