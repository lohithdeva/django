from django.views.generic import ListView, DetailView
from . models import Topic, SubTopic

class BlogListView(ListView):
    model = Topic
    template_name = 'home.html'

class SubBlogDetailView(DetailView):
    model = SubTopic
    template_name = 'subtopic_home.html'
    context_object_name = 'object'

class QuestionBlogDetailView(DetailView):
    model = Question
    template_name = 'question_home.html'
    context_object_name = 'list'
