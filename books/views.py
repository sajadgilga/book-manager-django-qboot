import json

import django as django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from books.models import Book
from books.serializers import BookEncoder


@method_decorator(csrf_exempt, name='dispatch')
class CreateBookView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        return JsonResponse({'message': 'not authenticated'}, status=401)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        name, text = data['name'], data['text']
        book, created = Book.objects.get_or_create(name=name, text=text, owner=request.user)
        return JsonResponse({'message': 'created successfully' if created else 'book already exists', 'data': book},
                            safe=False, encoder=BookEncoder)


class RetrieveBookView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            return JsonResponse({'message': 'success', 'data': book}, safe=False, encoder=BookEncoder)
        except Book.DoesNotExist:
            return JsonResponse({'message': 'not found'}, status=404)
