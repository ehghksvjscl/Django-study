from django.shortcuts import render
from . import models

def post_list(request):
    qs = models.Post.objects.all()
    content = {'post_list' : qs}
    return render(request,'blog1/post_list.html',content)