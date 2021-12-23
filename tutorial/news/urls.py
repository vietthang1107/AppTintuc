from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news.views import NewDetail, NewList, CommentList


urlpatterns = [
    path('news/', NewList.as_view()),
    path('news/<id>', NewDetail.as_view()),
    path('comments/', CommentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
