from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, Participant, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        print(data)
        return data

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'start_date', 'end_date', 'organizer', 'capacity', 'created_date']

    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event start date cannot be in the past.")
        return value

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'user', 'event', 'registered_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'event', 'message', 'created_at']
