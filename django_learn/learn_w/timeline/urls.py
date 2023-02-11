from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('timelines/', views.timeline_list),
    path('timelines/<int:pk>/', views.timeline_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

