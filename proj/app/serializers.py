# app/serializers.py
from rest_framework import serializers
from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name','last_name', 'email','username', 'password', 'salt']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(LoginSerializer, self).validate(attrs)

        # Custom data included in the response
        data.update({"id": self.user.id})
        data.update({"first_name": self.user.first_name})
        data.update({"last_name": self.user.last_name})
        data.update({"username": self.user.username})
        data.update({"email": self.user.email})
        return data
