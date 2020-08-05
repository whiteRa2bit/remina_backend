from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Item


def _success(data=None):
    response_dict = {'ok': True, 'errors': {}}
    if data is not None:
        response_dict['data'] = data
    return JsonResponse(response_dict)


def _error(errors, status=400):
    return JsonResponse({'ok': False, 'errors': errors}, status=status)


@csrf_exempt
@require_http_methods(['POST'])
def add_item(request):
    name = request.GET.get('name', '')
    topic = request.GET.get('topic', '')
    link = request.GET.get('link', '')
    rate = request.GET.get('rate', '')
    item = Item(name=name, topic=topic, link=link, rate=rate)
    item.save()

    return _success({'item': item.to_dict()})
