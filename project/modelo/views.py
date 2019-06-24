from django.shortcuts import render_to_response, render
from django.utils import timezone
import datetime
from django.http import Http404, HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import MySQLdb
from django.shortcuts import render

def lista_post(request):
    listado = Post.objects.order_by('nombre')
    return render_to_response('posting.html', {'lista_libros': lista_libros})


"""def post_list(request):
    posts = Post.objects.order_by('-created_date')[:10]
    return render_to_response( 'modelo/post_list.html', {'posts':posts})"""



def hola(request):
    HTML ="<body><h1>¡Hola Mundo!</h1></body></html>"
    return HttpResponse(HTML)

"""def fecha_actual(request):
    ahora = datetime.datetime.now()
    t = get_template('post_list.html')
    html = t.render({'fecha_actual': ahora})
    return HttpResponse(html)"""


def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': horas })
