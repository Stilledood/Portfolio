from django.db import models
from django.shortcuts import reverse


class Project(models.Model):
    '''Class to construct the model for all projects'''

    title=models.CharField(max_length=255)
    initial_description=models.TextField()
    project_description=models.TextField()
    summary_description=models.TextField()
    image1=models.ImageField(upload_to='project_images',default=None)
    image2=models.ImageField(upload_to='project_images',default=None)
    image3=models.ImageField(upload_to='project_images',default=None)
    github_link=models.URLField(max_length=255)
    live_demo_link=models.URLField(max_length=255)

    class Meta:
        ordering=['title',]
        get_latest_by='title'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details',kwargs={'pk':self.pk})




