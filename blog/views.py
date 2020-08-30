from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostCreateView(CreateView):
	model = Post
	fields = ['title','author','date','body',]
	def get_success_url(self):
		return reverse('blog:detail',args=[self.object.pk])
# Create your views here.
