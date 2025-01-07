from django.core.exceptions import PermissionDenied

class UserIsAdminOrModerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role != 'admin' and self.request.user.role != 'moderator':
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


