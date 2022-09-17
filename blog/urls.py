from . import views
from django.urls import path

urlpatterns = [
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('cocktails/', views.CocktailsList.as_view(), name='cocktails_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.Homepage.as_view(), name='home'),
]