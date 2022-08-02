"""Trips_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from Trips_app import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("trip-list/",views.TripListView.as_view()),
    path("trip-details/<int:trip_id>/",views.TripObjAPIView.as_view()),
    path("trip-update/<int:trip_id>/",views.TripObjUpdateView.as_view()),
    path("trip-cancel/<int:trip_id>",views.TripDeleteApiView.as_view()),
    path("trip-add/",views.TripObjAddView.as_view()),
    path("register/",views.RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    #urlpatterns += media (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




