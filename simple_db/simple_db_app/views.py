from django.shortcuts import render
from simple_db_app.models import Record

from django.http import HttpResponse
from django.views import View

# Create your views here.
def list(request):
    records=Record.objects.all()
    return render(request,
                'list.html',
                {
                    'records':records,
                })


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("'hello' URL")
    

class ByeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("'Bye!!!!!!!!' URL")    

