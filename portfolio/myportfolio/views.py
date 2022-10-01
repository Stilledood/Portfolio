from django.shortcuts import render
from .models import Project,ProjectCategory
from django.views.generic import View
from django.shortcuts import get_object_or_404


class GeneralView(View):
    '''Class to construct a vierw for homepage'''
    model=Project
    template_name='base.html'

    def get(self,request):
        online_store=self.model.objects.get(title__iexact='IFurniture')
        news_aggregator=self.model.objects.get(title__iexact='DinamoNews')
        scrapper=self.model.objects.get(title__iexact='Listing Scraper')
        twitter=self.model.objects.get(title__iexact='BitcoinWhale')
        api=self.model.objects.get(title__iexact='Drones Api')
        imaging=self.model.objects.get(title__iexact='Imaging Software')
        return render(request,self.template_name,context={'online_store':online_store,'dinamo_news':news_aggregator,'scrapper':scrapper,'twitter':twitter,'api':api,'imaging':imaging})





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
        technologies_image=project.projectimage_set.get(name='techs')

        return render(request,self.template_name,context={'project':project,'techs':technologies_image})

class WebApps(View):
    '''Class to construct a view to display a list of all webapps'''

    template_name='myportfolio/webapps.html'
    model=ProjectCategory

    def get(self,request):
        projects=self.model.objects.get(name__iexact='WebApp').project_set.all()

        return render(request,self.template_name,context={'projects':projects})


class Apps(View):
    '''Class to construct a view to display all projects with category=apps'''

    template_name='myportfolio/apps.html'
    model=ProjectCategory

    def get(self,request):
        projects=self.model.objects.get(name__iexact='App').project_set.all()


        return render(request,self.template_name,context={'projects':projects})


