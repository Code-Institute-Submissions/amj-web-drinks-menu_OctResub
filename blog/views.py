from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.template import loader
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def frontpage(request):
    template = loader.get_template('frontpage.html')
    return HttpResponse(template.render())


class AddPostView(View):
    def post(self, request, *aggs, **kwargs):
        author = request.user
        if author.has_perm('blog.add_post'):
            new_post = PostForm(request.POST, request.FILES)
            # new_post = PostForm(initial={
            #     'title': request.POST['title'],
            #     'featured_image': request.POST['featured_image'],
            #     'excerpt': request.POST['excerpt'],
            #     'content': request.POST['content'],
            #     'status': request.POST['status'],
            # })
            post_save = new_post.save(commit=False)
            post_save.slug = slugify(request.POST['title'])
            post_save.author = author
            post_save.save()
            return redirect('/')

        template_name = 'add_post.html'
        context = {
            message: 'You do not have permission to post',
            form: PostForm
            }
        return render(request, template_name, context)
        
    def get(self, request): 
        template_name = 'add_post.html'
        context = {
            'form': PostForm,
            'message': ''  
        }
        return render(request, template_name, context)
