from django.urls import re_path
from .views import ProjectList,ProjectDetails

urlpatterns=[
    re_path(r'^$',ProjectList.as_view(),name='project_list'),
    re_path(r'^(?P<pk>\d+)/$',ProjectDetails.as_view(),name='product_details')
]