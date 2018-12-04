from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from blog.models import Post, Author
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    template_name = "index.html"
    posts = Post.objects.filter(published=True).order_by('-date')
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)


def post(request, id):
    template_name = "post.html"
    try:
        post = get_object_or_404(Post, id=id, published=True)
        context = {'post': post}
        return render(request=request, template_name=template_name, context=context)
    except:
        return HttpResponse("the post doesn't exist")


@login_required(login_url="/admin")
def new(request):
    form = (PostForm(request.POST) or None)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            post = form.save(commit=False)
            post.author = author
            post.published_date = timezone.now()

            post.save()
            return redirect("post", id=post.id)
    elif request.method == "GET":
        template_name = "new_post.html"
        posts = Post.objects.filter(published=True)
        context = {'posts': posts}
        return render(request=request, template_name=template_name, context=context)
