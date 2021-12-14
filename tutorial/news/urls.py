from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views


urlpatterns = [
    path('news/', views.new_list),
    path('news/<int:pk>', views.new_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
