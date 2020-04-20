from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self, **kwargs):
        import users.signals
