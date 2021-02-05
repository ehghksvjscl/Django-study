from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from .models import Post
from .forms import PostForm
from django.http import HttpRequest, HttpResponse, Http404

def post_new(request):
    form = PostForm()
    return render(request,'instagram/post_form.html',{'form':form})

# post_list = login_required(ListView.as_view(model=Post,paginate_by=10))

# @method_decorator(login_required,name='dispatch')
class PostListView(LoginRequiredMixin,ListView):
    model=Post
    paginate_by=10

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#    qs = Post.objects.all()
#    q = request.GET.get('q','')
#    print("asdasdasdasd")

   # instagram/templates/instagram/post_list.html
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

# def archives_year(request,year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at',paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at',make_object_list=True)

