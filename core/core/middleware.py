from datetime import datetime


class UserLastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            u = request.user
            u.last_request = datetime.now()
            u.save()
        response = self.get_response(request)
        return response
