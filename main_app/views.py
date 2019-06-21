from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Skill

# Create your views here.
def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})


class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    success_url = '/'

class SkillDelete(DeleteView):
    model = Skill
    fields = '__all__'
    success_url = '/'
