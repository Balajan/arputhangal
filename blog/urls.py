from django.urls import path
from .views import PostDetailView,PostCreateView
from .views import PostDetail

app_name ='blog'

urlpatterns = [
	path('<int:pk>/',PostDetailView.as_view(),name='detail'),
	path('raw/<int:pk>/',PostDetail.as_view(),name='detailraw'),
	path('create/',PostCreateView.as_view(),name='create'),
]