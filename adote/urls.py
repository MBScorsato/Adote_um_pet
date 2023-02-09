"""adote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crudsimples.views import ProdutoNovo, ProdutoLista, ProdutoAtualizar, ProdutoDetalhe, ProdutoApagar
from usuarios.views import home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include('usuarios.urls')),
                  path('', home, name='home'),
                  path('divulgar/', include('divulgar.urls')),
                  path('adotar/', include('adotar.urls')),
                  ##### url crud simples ####
                  path('produto/novo/', ProdutoNovo.as_view(), name='produto-novo'),
                  path('produto/lista/', ProdutoLista.as_view(), name='produto-lista'),
                  path('produto/<int:pk>/atualizar/', ProdutoAtualizar.as_view(), name='produto-atualizar'),
                  path('produto/<int:pk>/detalhe/', ProdutoDetalhe.as_view(), name='produto-detalhe'),
                  path('produto/apagar/<int:pk>/', ProdutoApagar.as_view(), name='produto-apagar'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
