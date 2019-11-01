from rest_framework.permissions import BasePermission
P={ 'IsAuthenticated':IsAuthenticated,
    'IsAdminUser':IsAdminUser,
    'IsModeratorUser':IsModeratorUser,
    'IsUser':IsUser,
    'ModeratorOrOwner':ModeratorOrOwner}


class AllowAny(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self,request, view ):
        return bool(True is True)

class IsAuthenticated:
    """
    Allows access only to authenticated users.
    """

    def has_permission(user):
        return bool(user and user.is_authenticated)

class IsAdminUser:

    def has_permission(user):
        if (user.is_admin == True) and (user.is_moderator == True):
            return False
        else:
            return bool(user and user.is_admin)

class IsStaffUser:
    
    def has_permission(user):
        if (user.is_admin == True) or (user.is_moderator == True):
            return True
        else:
            return False

class IsModeratorUser:
    """
    Allows access only to moderator users.
    """

    def has_permission(user):
        return bool(user and user.is_moderator)

class IsUser:

    def has_object_permission(user,obj):
        if (user.is_authenticated == True) and (user.get('id') = obj.get('id')):
            return True
        else:
            return False

class IsModeratorOrOwner:

    def has_permission(user):
        if (user.is_moderator == True) or (user.is_owner == True):
            return True
        else:
            return False
