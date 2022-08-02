from rest_framework import serializers
from .models import Trip
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken






# Register User 
User = get_user_model()

class UserRegisterserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","password",]

    def create (self,validated_data):
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
            #create profile

        return validated_data


# login User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)


    def validate(self,data):
        username = data.get("username")
        password = data.get("password")

        try:
            user= User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValudationError("Username Dose not exist !")


        if not user.check_password(password):
            raise serializers.ValidationError("Wrong Password ! Try again")


        payload = RefreshToken.for_user(user)


        token = str(payload.access_token)
        data["accsess"] = token

        return data





class TripListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"



class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"