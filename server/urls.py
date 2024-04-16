from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from server import views

urlpatterns = [
    path('municipalities/', views.MunicipalityList.as_view()),
    path('municipalities/<int:pk>/', views.MunicipalityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)