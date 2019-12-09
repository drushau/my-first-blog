from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^formulario/$',views.formulario,name="formulario"),
    url(r'^eventos/$',views.eventos,name="eventos"),
    url(r'^noticias/$',views.noticias,name="noticias"),
    url(r'^about/$',views.about,name="about"),
]