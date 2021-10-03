import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template import loader
from bizu.models import User

@csrf_exempt
@require_POST
def process(request):
    print(request.body)
    out = json.loads(request.body if request.body else "{}")
    event = out['event']
    print(event)
    print(type(event))

    new_user = User(name=event['nome_fantasia'], email=event['email'], endereco=event['endereco'], cidade=event['cidade'])
    new_user.save()

    print("New user was saved: ")
    print(new_user)
    return HttpResponse("user was saved")

def index(request):
    users = User.objects.all()
    print(users)
    template = loader.get_template('index.html')

    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))
