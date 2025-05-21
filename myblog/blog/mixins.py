from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyUserMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user
