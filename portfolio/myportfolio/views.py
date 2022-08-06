from django.shortcuts import render
from .models import Project
from django.views.generic import View



class ProjectList(View):
    '''Class to construct a view to display all projects'''

    model=Project
    template_name='myportfolio/project_list.html'

    def get(self,request):
        project_list=self.model.objects.all()
        return render(request,self.template_name,context={'project_list':project_list})



    