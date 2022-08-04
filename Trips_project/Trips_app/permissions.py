from rest_framework.permissions import BasePermission

class IsUser (BasePermission):

    def has_object_permissions(self,request,view,obj):
        return request.user == obj.user or request.user.is_staff
