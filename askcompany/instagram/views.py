from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.http import HttpRequest, HttpResponse

post_list = ListView.as_view(model=Post)
 
# def post_list(request):
#    qs = Post.objects.all()
#    q = request.GET.get('q','')
#
#    # instagram/templates/instagram/post_list.html
#    if q:
#        qs = qs.filter(message__icontains=q)
#    return render(request, 'instagram/post_list.html',{'post_list' : qs})

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello Wolrd")
    response.write("Hello Wolrd")
    response.write(pk)
    return response

def archives_year(request,year):
    return HttpResponse(f"{year}년 archives")
