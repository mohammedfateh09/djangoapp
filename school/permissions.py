from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        print( request.user.role)
        if request.method in permissions.SAFE_METHODS and request.user.role !='student':
            return True
        # return obj.user == request.user
        
