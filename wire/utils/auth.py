import json
from wire.utils.hasher import Hasher, HashMismatch
from wire.models.user import User

class Auth:
    def __init__(self, redis):
        self.redis = redis
        self.user = False
    def attempt(self, username, password):
        r = self.redis
        h = Hasher()
        if not r.exists('username:%s' % username):
            raise AuthError()

        key = r.get('username:%s' % username)
        data = json.loads(r.get('user:%s' % key))
        try:
            h.check(password, data['password'])
        except HashMismatch:
            raise AuthError()
        self.user = User(data=data, redis=r, key=key)
    def set_user(self, user):
        self.user = user

    def action(self, action, id=False):
        pass

class AuthError(Exception):
    pass

class DeniedError(AuthError):
    pass