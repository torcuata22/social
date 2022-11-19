from django.shortcuts import render
from .forms import PostCreateForm

# Create your views here.
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit_to = False) #won't commit yet
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)

    return render(request, 'post/create.html', {'form' : form})