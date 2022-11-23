from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files = request.FILES)
        if form.is_valid():
            new_item = form.save(commit = False) #won't commit yet
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)

    return render(request, 'posts/create.html', {'form' : form})


def feed(request):
    posts = Post.objects.all()
    return render(request, 'posts/feed.html',{'posts':posts})

def like_post(request):
    post_id = request.post.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exitst(): #post already been liked
        post.liked_by.remove(request.user)
    else: #post has not been liked
        post.liked_by.add(request.user)

    return redirect('feed')


    