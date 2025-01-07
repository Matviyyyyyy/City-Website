from django.core.exceptions import PermissionDenied


class UserIsHisProfileMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != self.request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class UserIsAdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
