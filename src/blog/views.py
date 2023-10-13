from django.http import Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"blog/index.html")

def article(request, number_article):
    if number_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{number_article}.html")

    else:
        #raise Http404("L'article demandé n'a pas été trouvé")
        return render(request, f"blog/article_not_found.html")
   
