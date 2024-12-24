from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Event, Notification, Participant
from .serializers import EventSerializer, ParticipantSerializer, NotificationSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User

class UserCreateView(generics.CreateAPIView):
    """
    Handle user registration and account creation.
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Override the post method to handle user creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EventViewSet(viewsets.ModelViewSet):
    """
    Handle CRUD operations for events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return events filtered by the logged-in user's username as the organizer.
        """
        return Event.objects.filter(organizer=self.request.user.username)

    def perform_create(self, serializer):
        """
        Override the perform_create method to automatically set the organizer.
        """
        serializer.save(organizer=self.request.user.username)

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        """
        Register a user for an event.
        """
        event = self.get_object()
        if event.is_full():
            return Response({"detail": "Event is full."}, status=status.HTTP_400_BAD_REQUEST)
        participant = Participant.objects.create(user=request.user, event=event)
        return Response(ParticipantSerializer(participant).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def unregister(self, request, pk=None):
        """
        Unregister a user from an event.
        """
        event = self.get_object()
        participant = Participant.objects.filter(user=request.user, event=event).first()
        if participant:
            participant.delete()
            return Response({"detail": "Successfully unregistered."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

class ParticipantViewSet(viewsets.ModelViewSet):
    """
    Handle CRUD operations for participants.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    """
    Handle CRUD operations for event notifications.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]