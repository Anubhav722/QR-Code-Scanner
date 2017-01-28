from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.
#
# class UserCreate(CreateView):
#     form_class = UserProfileForm
#     model = UserProfile
#
#     fields = ['user', 'description']

class IndexView(ListView):
    queryset = UserProfile.objects.all()
    template_name = 'index.html'
    # by default the name of the template will be tweet_list.html
    def get_context_data(self, *args, **kwargs):
        context= super(IndexView, self).get_context_data(*args, **kwargs)
        #print (context)
        return context

