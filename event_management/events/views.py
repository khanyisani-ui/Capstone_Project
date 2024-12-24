from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, Participant, Notification
from .serializers import EventSerializer, ParticipantSerializer, NotificationSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsAdminOrOrganizer


# User Registration
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        }, status=201)


# User Login (JWT)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = User.objects.get(username=data['username'])
        if user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=200)
        return Response({"detail": "Invalid credentials"}, status=400)


# Event Management
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOrganizer]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user.username)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_participant(self, request, pk=None):
        event = self.get_object()
        if event.is_full():
            return Response({"detail": "Event is full"}, status=400)
        
        participant = Participant.objects.create(user=request.user, event=event)
        return Response(ParticipantSerializer(participant).data, status=201)


# Participant Management
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event_id = self.request.query_params.get('event_id')
        if event_id:
            return Participant.objects.filter(event_id=event_id)
        return Participant.objects.all()


# Notification System
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def send_notification(self, request, pk=None):
        event = Event.objects.get(id=pk)
        message = request.data.get("message")
        notification = Notification.objects.create(user=request.user, event=event, message=message)
        return Response(NotificationSerializer(notification).data, status=201)


# Search Events
class EventSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.all()
        date = request.query_params.get('date')
        location = request.query_params.get('location')

        if date:
            events = events.filter(start_date__date=date)
        if location:
            events = events.filter(location__icontains=location)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
