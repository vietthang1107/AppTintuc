from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news.views import NewDetail, NewList


urlpatterns = [
    path('news/', NewList.as_view()),
    path('news/<int:pk>', NewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
