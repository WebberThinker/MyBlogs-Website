from django.shortcuts import render
from .models import Post, Contact
from django.views.generic import ListView, DetailView, CreateView
from .forms import ContactForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.order_by('-post_date')[:2]  # Get the 2 most recent posts
        return context


class BlogView(ListView):
    model = Post
    template_name = "blogs.html"

class DetailPageView(DetailView):
    model = Post
    template_name = "detail_page.html"

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"

def RecentPostView(request):
    recent_post = Post.objects.order_by('post_date')[:2]
    context = {'recent_post': recent_post}
    return render(request, 'recent_post.html', context)

def AboutView(request):
    return render(request, 'about.html', {})

