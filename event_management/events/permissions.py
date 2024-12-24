from rest_framework import permissions


class IsAdminOrOrganizer(permissions.BasePermission):
    """
    Custom permission to allow only admins and event organizers to edit events.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:  # Admin check
            return True
        return request.user.groups.filter(name='Event Organizers').exists()  # Event organizer check
