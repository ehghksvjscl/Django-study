from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')

    # instagram/templates/instagram/post_list.html
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html',{'post_list' : qs})

