from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import Trip
from .serializer import TripListSerializer,DetailSerializer,UpdateSerializer,UserRegisterserializer,CreateSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import serializers
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


# view details for a trip using id
class TripObjAPIView(RetrieveAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    serializer_class = DetailSerializer



# update trip 
class TripObjUpdateView(UpdateAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    serializer_class = UpdateSerializer
    permission_classes = ["IsAuthenticated"]


# delete trip
class TripDeleteApiView(DestroyAPIView):
    queryset = Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"


# create trip
class TripObjAddView(CreateAPIView):
    serializer_class = CreateSerializer
    # def perform_create(self,obj):
    #     return None
    

