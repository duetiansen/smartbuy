from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^home$', views.index, name='index'),
    url(r'^mail$', views.mail, name='mail'),
    url(r'^products$', views.products, name='products'),
    url(r'^products1$', views.products1, name='products1'),
    url(r'^products2$', views.products2, name='products2'),
    url(r'^codes$', views.codes, name='codes'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^icons$', views.icons, name='icons'),
]
