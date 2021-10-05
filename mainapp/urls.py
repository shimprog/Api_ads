from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mainapp import views


urlpatterns = [
    path('api/', views.AdvertList.as_view()),
    path('api/create/', views.AdvertCreate.as_view()),
    path('api/<int:pk>/', views.AdvertDetail.as_view()),
    path('api/<int:pk>/fields/', views.AdvertDetailFull.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
