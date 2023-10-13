
from .views import index
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', index, name = "index"),
    path('blog/', include("blog.urls")),#Inclusion des schémas d'URL définis dans le fichier urls.py de l'application "blog"  dans le schéma d'URL global de votre projet
    path('admin/', admin.site.urls),
    
]
