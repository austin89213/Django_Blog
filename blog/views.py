from django.shortcuts import render, get_object_or_404,redirect
from django.http import  HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic.edit import FormMixin
from django.template.loader import render_to_string
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,
                                    )
class IndexPage(TemplateView):
    template_name = 'blog/index.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author =self.request.user
        post.save()
        return redirect('blog:post_detail',pk=post.pk)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class AnalysisDetailView(DeleteView):
    model = Post
    template_name = 'blog/analysis_detail.html'


def analysis_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context ={
        'post':post,
    }
    if request.is_ajax():
        html = render_to_string('blog/pie_chart.html', context=context, request=request)
        return JsonResponse({'form':html})
    return render(request,'blog/analysis_detail.html',context)


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method =='GET':
        post.viewed()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    context ={
        'post':post,
        'comments':comments,
        'form':form
    }
    if request.is_ajax():
        html = render_to_string('blog/comments.html', context=context, request=request)
        return JsonResponse({'form':html})
    return render(request,'blog/post_detail.html',context)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'accounts/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("blog:post_list")
