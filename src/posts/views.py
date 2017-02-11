from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def posts_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "form":form,
    }

    return render(request, "post_form.html", context)

def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "object": instance      
    }

    return render(request, "post_detail.html", context)

def posts_list(request):
    queryset = Post.objects.all()

    context = {
        "object_list": queryset,
        "title": "Detail"
    }

    return render(request, "post_list.html", context)

def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "object": instance,
        "form": form,
    }

    return render(request, "post_form.html", context)

def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted")
    return redirect("posts:list")

