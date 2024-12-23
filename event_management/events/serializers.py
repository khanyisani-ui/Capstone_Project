# events/serializers.py
from rest_framework import serializers
from .models import Event, Participant, Notification
from django.contrib.auth.models import User
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to handle registration and login.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Override the create method to hash the user's password before saving.
        """
        user = User.objects.create_user(**validated_data)
        return user

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model to validate and transform event data.
    """
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'start_date', 'end_date', 'organizer', 'capacity', 'created_date']

    def validate_start_date(self, value):
        """
        Ensure the event start date is not in the past.
        """
        if value < timezone.now():
            raise serializers.ValidationError("Event start date cannot be in the past.")
        return value

class ParticipantSerializer(serializers.ModelSerializer):
    """
    Serializer for the Participant model to transform participant data.
    """
    class Meta:
        model = Participant
        fields = ['id', 'user', 'event', 'registered_at']

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model to transform notification data.
    """
    class Meta:
        model = Notification
        fields = ['id', 'user', 'event', 'message', 'created_at']
