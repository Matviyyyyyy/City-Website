from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class UserIsModeratorOrAdmin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "moderator" and request.user.role != "admin":
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
