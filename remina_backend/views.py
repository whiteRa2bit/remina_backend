from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def dumb_endpoint(request):
    return JsonResponse({'title': 'hi'})
