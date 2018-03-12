from rest_framework.permissions import BasePermission
from . import models

class IsOwner(BasePermission):


    def has_object_permission(self, request, view, obj):
        if isinstance(obj, models.Todo):
            return obj.created_by == request.user
        return obj.created_by == request.user
