import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        try:
            username, password = data['username'], data['password']
        except:
            return JsonResponse({'message': 'wrong login parameters'}, status=400)
        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({'message': 'wrong credentials'}, status=400)
        login(request, user)
        return JsonResponse({'message': 'success'})
