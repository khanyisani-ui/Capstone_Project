from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.CharField(max_length=100)  
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def is_full(self):
        """
        Checks if the event is full based on the number of participants.
        """
        return self.participants.count() >= self.capacity

    def __str__(self):
        """
        String representation of the Event model.
        """
        return self.title

class Participant(models.Model):
    """
    Model for participants registering for events.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Participant model.
        """
        return f"{self.user.username} - {self.event.title}"

class Notification(models.Model):
    """
    Model to manage notifications for users about events.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Notification model.
        """
        return f"Notification for {self.user.username} about {self.event.title}"

