from threading import local

_thread_locals = local()


def set_current_user(user):
    setattr(_thread_locals, "user", user)


def get_current_user():
    return getattr(_thread_locals, "user", None)


def get_current_accounts():
    return getattr(_thread_locals, "accounts", None)


def set_current_accounts(accounts):
    setattr(_thread_locals, "accounts", accounts)


class ThreadLocals:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        self.process_request(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        user = getattr(request, "user", None)

        if user is not None and not user.is_anonymous:
            set_current_user(user)
            set_current_accounts(user.accounts)
