from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (ListView, 
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView,
                                )   
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):

    # this function is overwriting the above function
    model = Post 
    # if you left it upto here only you will get an error becuase by defalt class based view look for tenplates in certain naming pattern => <app/model>_<viewtype>.html
    # since here , app = blog , model = post, viewtype = list ==> blog/post_list.html 
    template_name = 'blog/home.html'
    context_object_name = 'posts' # or name will be post_object
    ordering = ['-date_posted'] # to see the latest post on the top
    paginate_by = 5
    # In class based views , just setting up few variable will do our work
    # 

class UserPostListView(ListView):
    model = Post 
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    #ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') # therefore comment above

      

class PostDetailView(DetailView):
    model = Post 
    # according to naming convinction it will look into blog/post_detail.html because detail is the viewtype here.


#@login_required cannot be used as it is not a function view it is a class view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post    
    # blog/post_create.html will be required. not here but blogs/post_form.html

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    
    # blog/post_create.html will be required. not here but blogs/post_form.html

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # method for user test if the current login user is equal to thwe author of the post who is trying to update  
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else :
            return False

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin,   DeleteView):
    model = Post
    success_url = '/'      
    def test_func(self): # method for user test if the current login user is equal to thwe author of the post who is trying to update  
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else :
            return False

            


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})    
    
# list view can be used to list all the content of a webpage
# detail view can be used to take to the user to one of the list view he has clicked

""" 
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)  this function has been replace by the list view  """

