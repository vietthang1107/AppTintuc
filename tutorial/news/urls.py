from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views


urlpatterns = [
    path('news/', views.NewList.as_view()),
    path('news/<int:pk>', views.NewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
