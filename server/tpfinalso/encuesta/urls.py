from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<preg>\d+)/$',views.preguntaID, name='pregunta por id'),
    url(r'^question/$', views.preguntaAll, name='todas preguntas'),
    url(r'^choice/(?P<preg>\d+)/$', views.opcionesPorPregunta, name='opciones de pregunta')
]
