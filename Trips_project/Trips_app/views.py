from cProfile import Profile
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import Trip,Profile
from .serializer import TripListSerializer,DetailSerializer,UpdateSerializer,UserRegisterserializer,CreateSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import serializers
from .permissions import IsUser
# Create your views here.




           

#register view
class RegisterUserView(CreateAPIView):
    serializer_class = UserRegisterserializer


# Login
class LoginView():
    pass


#View all Trips
class TripListView(ListAPIView):
    queryset =Trip.objects.all()
    serializer_class = TripListSerializer
    permission_classes = ["IsAuthenticated","IsUser"]


# view details for a trip using id
class TripObjAPIView(RetrieveAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    serializer_class = DetailSerializer
    permission_classes = ["IsAuthenticated","IsUser"]



# update trip 
class TripObjUpdateView(UpdateAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    serializer_class = UpdateSerializer
    permission_classes = ["IsAuthenticated","IsUser"]


# delete trip
class TripDeleteApiView(DestroyAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    permission_classes = ["IsAuthenticated","IsUser"]


# create trip
class TripObjAddView(CreateAPIView):
    serializer_class = CreateSerializer
    # def perform_create(self,obj):
    #     return None
    

"""
Profile API 

"""


class ProfileObjAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "profile_id"
    serializer_class = DetailSerializer

class ProfileObjUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "profile_id"
    serializer_class = UpdateSerializer
    permission_classes = ["IsAuthenticated"]