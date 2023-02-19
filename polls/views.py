import smtplib, ssl
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import FormUpdatePost
from .models import Post, Comment
from .settings import SENDER_EMAIL, SMTP_SERVER, SMTP_PORT, EMAIL_PASSWORD


class IndexView(LoginRequiredMixin, generic.ListView):
    paginate_by = 24
    login_url = '/accounts/login/'
    template_name = 'polls/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(post_isdeleted=False).all().order_by('-post_created')


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            post_id=context['post'].id, comment_isdeleted=False).all().order_by('-comment_created')
        return context


class PostSearchView(LoginRequiredMixin, generic.ListView):
    paginate_by = 24
    login_url = '/accounts/login/'
    template_name = 'polls/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        content = self.request.GET['content']
        posts = self.model.objects.all().order_by('-post_created')
        if content:
            posts = posts.filter(
                Q(post_content__contains=content) | Q(post_title__contains=content)).all().order_by('-post_created')
        return posts


class PostViewByUser(LoginRequiredMixin, generic.ListView):
    paginate_by = 12
    login_url = '/accounts/login/'
    template_name = 'polls/posts_by_user.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        author = self.request.user
        posts = self.model.objects.filter(
            author=author, post_isdeleted=False).all().order_by('-post_created')
        return posts


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'polls/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('polls:mypost')


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'polls/update_post.html'
    form_class = FormUpdatePost
    success_url = reverse_lazy('polls:mypost')


class CreatePostView(LoginRequiredMixin, generic.View):
    login_url = '/accounts/login/'

    def post(self, request):
        title = self.request.POST['title']
        content = self.request.POST['content']
        post = Post(post_title=title, post_content=content,
                    author=request.user)
        post.save()
        messages.success(request, 'Create new post successful')
        return redirect('polls:index')


class CreateCommentView(LoginRequiredMixin, generic.View):
    login_url = '/accounts/login/'

    def post(self, request, post_id):
        comment_content = self.request.POST['comment']
        post = Post.objects.get(id=post_id)
        post.post_comment_count = F('post_comment_count') + 1
        comment = Comment(author=request.user, post=post,
                          comment_content=comment_content)
        post.save()
        comment.save()
        return redirect('polls:detail', pk=post_id)


class SenMailView(LoginRequiredMixin, generic.View):
    login_url = '/accounts/login/'
    template_name = 'polls/sendmail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, *args, **kwargs):
        try:
            receiver_email = self.request.POST['email']
            message = self.request.POST['message']
            message_error = 'Send email fail!'
            if receiver_email and message:
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT, context=context) as server:
                        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
                        server.sendmail(SENDER_EMAIL, receiver_email, message)
                    message_success = 'Email is sent successfully!'
                    return JsonResponse({'message': message_success}, status=200)
                except Exception:
                    return JsonResponse({'message_error': message_error}, status=400)
            else:
                return JsonResponse({'message_error': message_error}, status=400)
        except Exception:
            return JsonResponse({'message_error': 'Sever error!'}, status=500)
