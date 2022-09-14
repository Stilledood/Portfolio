from django.shortcuts import render
from .models import Project
from django.views.generic import View
from django.shortcuts import get_object_or_404


class GeneralView(View):
    '''Class to construct a vierw for homepage'''
    model=Project
    template_name='base.html'

    def get(self,request):
        first_projects=Project.objects.all()
        return render(request,self.template_name,context={'first_projects':first_projects})





class ProjectList(View):
    '''Class to construct a view to display all projects'''

    model=Project
    template_name='myportfolio/project_list.html'

    def get(self,request):
        project_list=self.model.objects.all()
        return render(request,self.template_name,context={'project_list':project_list})




class ProjectDetails(View):
    '''Class to construct a view to display all informations about a project'''

    model=Project
    template_name='myportfolio/project_details.html'

    def get(self,request,pk):
        project=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,context={'project':project})

