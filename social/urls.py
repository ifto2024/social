from django.contrib import admin
from django.urls import path,include, re_path
from socialapp.views import index, sobre, postar,contato, new_avalia, editar_avalia, deleta_avalia
from socialapp.views import new_post, deleta_post, editar_post

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('postar/', postar, name='postar'),
    path('contato/', contato, name='contato'),
    path('new_avalia/', new_avalia, name='new_avalia'),
    path('editar_avalia/<str:id>', editar_avalia, name='editar_avalia'),
    path('deleta_avalia/<int:id>', deleta_avalia, name='deleta_avalia'),
    #post
    path('new_post/', new_post, name='new_post'),
    path('editar_post/<str:id>', editar_post, name='editar_post'),
    path('deleta_post/<int:id>', deleta_post, name='deleta_post'),

    path('', include('usuario.urls')),



]
