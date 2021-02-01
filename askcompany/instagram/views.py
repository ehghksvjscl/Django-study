from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404

post_list = ListView.as_view(model=Post)
 
# def post_list(request):
#    qs = Post.objects.all()
#    q = request.GET.get('q','')
#
#    # instagram/templates/instagram/post_list.html
#    if q:
#        qs = qs.filter(message__icontains=q)
#    return render(request, 'instagram/post_list.html',{'post_list' : qs})

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = get_object_or_404(Post,pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExit:
    #     raise Http404
    # return render(request, 'instagram/post_detail.html', {
    #     "post" : post,
    # },status=200)

post_detail = DetailView.as_view(model=Post)

def archives_year(request,year):
    return HttpResponse(f"{year}년 archives")
