from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','is_staff','is_superuser']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class DriversSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=120)
    surname = serializers.CharField(max_length=120)
    rating = serializers.CharField(max_length=120)
    class Meta:
        model = Drivers
        fields = ('id','name','surname','rating')
    def create(self, validated_data):
        return Drivers.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.surname = validated_data.get('surname',instance.surname)
        instance.rating = validated_data.get('rating',instance.rating)
        instance.save()
        return instance
class NewsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=120)
    photo = serializers.CharField(max_length=120)
    date = serializers.CharField(max_length=120)
    user = serializers.CharField(max_length=120)
    class Meta:
        model = News
        fields = ('id','title','description','photo','date','user')
    def create(self, validated_data):
        return News.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.photo = validated_data.get('photo',instance.photo)
        instance.date = validated_data.get('date',instance.date)
        instance.user = validated_data.get('user',instance.user)
        instance.save()
        return instance
class CarsSerializer(serializers.Serializer):
    id = serializers.CharField()
    mark = serializers.CharField(max_length=120)
    model = serializers.CharField(max_length=120)
    isValid = serializers.BooleanField()
    
    def create(self, validated_data):
        return Cars.objects.create(**validated_data)