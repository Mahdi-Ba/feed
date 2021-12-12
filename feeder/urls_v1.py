
from django.urls import path, include
urlpatterns = [
    path('users/', include('user.urls')),
    path('rss/', include('rssdriver.urls')),

]
