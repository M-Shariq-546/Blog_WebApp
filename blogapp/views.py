from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView
from blogs import settings
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (ListView
                                  , DetailView
                                  , CreateView
                                  , UpdateView
                                  , DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin 
from django.contrib.messages.views import SuccessMessageMixin




def index(request):
    data = {
        "posts" : Post.objects.all(),
    }
    return render(request, 'blogs/index.html' , data)


class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'#<app_name>/<ModelName>_<typeofdatatype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blogs/user_post.html'#<app_name>/<ModelName>_<typeofdatatype>.html
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# Post Details Class View
class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_details.html' 


# Post Creation View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogs/post_new_blog.html'
    fields = ['title' , 'content']

    # This is setting the instance author as user which is logged in
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# Pots Deletion Class View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # this is the url where user will go after successful deletion
    success_url = '/blog/'
    template_name = 'blogs/post_confirm_delete.html'

    # This is check post for the same user which is logged in
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Post updation class view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # Template name setting at here
    template_name = 'blogs/post_new_blog.html'
    # fields to update
    fields = ['title' , 'content']

    # This is setting the instance author as user which is logged in
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This is the function which is used for validating that user can access his posts and details only
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
'''
class EmailForReset(SuccessMessageMixin ,PasswordResetView):
   # template_name='users/reset-password.html'
  #  email_sending_template ='users/reset-password-email.html'
  #  subject_template_name = 'users/email_reset_subject.txt'
 #   success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should     receive                  them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and                    check your spam folder."
                      
#    success_url = '/reset-password/done/'
'''
# Our About page
def about(request):
    return render(request , "blogs/about.html" , {"title":"About us"})

''' 
   from django.conf import settings
    from django.core.mail import send_mail

    
    subject = 'welcome to GFG world'
    message = f'Hi, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['MShariq28022000@hotmail.com', ]
    send_mail(subject, message, email_from, recipient_list )
'''
    