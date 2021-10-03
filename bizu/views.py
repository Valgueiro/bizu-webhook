import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def process(request):
    print(request.body)
    out = json.loads(request.body if request.body else "{}")
    print(out)
    return HttpResponse(json.dumps(out))
