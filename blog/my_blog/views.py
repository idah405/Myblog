from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.
class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'list.html'

class Detail_view(generic.DeleteView):
    model = Post
    template_name = 'detail.html'
