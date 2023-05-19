from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request,'blogging/list.html', context)

class BloggingListView(ListView):
    queryset = Post.objects.order_by('-published_date')#.filter(published__date__exact=None)
    template_name = 'blogging/list.html'
    context_object_name = 'queryset'

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)

# class BloggingDetailView()
