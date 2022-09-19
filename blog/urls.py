from django.urls import path
from . import views


urlpatterns = [
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('cocktails/', views.CocktailsList.as_view(), name='cocktails_list'),
    path('delete_post/<int:id>/', views.DeletePost.as_view(), name='delete_post'),
    path('edit_post/<int:id>/', views.EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.Homepage.as_view(), name='home'),
]
