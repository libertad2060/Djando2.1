from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post
import datetime
from django.http import Http404, HttpResponse
from django.template import Template, Context
from django.template.loader import get_template



"""def post_list(request):
    posts = Post.objects.order_by('-created_date')[:10]
    return render_to_response( 'modelo/post_list.html', {'posts':posts})"""



def hola(request):
    HTML ="<body><h1>¡Hola Mundo!</h1></body></html>"
    return HttpResponse(HTML)

def fecha_actual(request):
    ahora = datetime.datetime.now()
    t = get_template('post_list.html')
    html = t.render({'fecha_actual': ahora})
    return HttpResponse(html)


def horas_adelante(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt= datetime.timedelta(offset)
    html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)
