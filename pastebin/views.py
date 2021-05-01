import self as self
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html", {'idn' : request.GET.get('idn')})

@csrf_exempt
def ajax(request):
    from pastebin.models import field
    res = 'fail'
    try :
        q = field(id=request.GET.get('id'), date=request.GET.get('date'), text=request.GET.get('text'))
        stat = q.save()
        res = 'success'
    except Exception as e :
        from pyexpat.errors import messages
        self.message_user(request, e, messages.ERROR)
        res = 'fail'
    return HttpResponse(res)

@csrf_exempt
def getajax(request):
    from pastebin.models import field
    res = 'fail'
    try :
        res = field.objects.get(id=request.GET.get('id')).text
    except Exception as e :
        from pyexpat.errors import messages
        self.message_user(request, e, messages.ERROR)
        res = 'fail'
    return HttpResponse(res)