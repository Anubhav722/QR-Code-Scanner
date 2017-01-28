from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView

from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.

class UserRegister(FormView):
    form_class = UserProfileForm
    model = UserProfile
    template_name = 'register.html'
    success_url = '/check/index/'

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
        user.save()
        return super(UserRegister, self).form_valid(form)
    # fields = ['user', 'description']

class IndexView(ListView):
    queryset = UserProfile.objects.all()
    template_name = 'index.html'
    # by default the name of the template will be tweet_list.html
    def get_context_data(self, *args, **kwargs):
        context= super(IndexView, self).get_context_data(*args, **kwargs)
        #print (context)
        return context

