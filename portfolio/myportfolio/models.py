from django.db import models
from django.shortcuts import reverse


class ProjectCategory(models.Model):
    '''Class to construct a model for project category'''

    name=models.CharField(max_length=128,unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_details',kwargs={'pk':self.pk})


class Project(models.Model):
    '''Class to construct the model for all projects'''

    title=models.CharField(max_length=255)
    initial_description=models.TextField()
    project_description=models.TextField()
    summary_description=models.TextField()
    main_image=models.ImageField(upload_to='project_images',default=None)
    github_link=models.URLField(max_length=255)
    live_demo_link=models.URLField(max_length=255,default=None)
    category=models.ForeignKey(ProjectCategory,on_delete=models.CASCADE)


    class Meta:
        ordering=['title',]
        get_latest_by='title'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details',kwargs={'pk':self.pk})




class ProjectImage(models.Model):
    '''Class to construct a model for projects images-allowing a project to have multiple images associated with'''

    name=models.CharField(max_length=128)
    image=models.ImageField(upload_to='project_images')
    project=models.ForeignKey(Project,on_delete=models.CASCADE)





