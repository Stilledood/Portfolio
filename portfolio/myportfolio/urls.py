from django.urls import path
from .views import ProjectList,ProjectDetails

urlpatterns=[
    path(r'^$',ProjectList.as_view(),name='project_list'),
    path(r'(?P<pk>\d+/$',ProjectDetails.as_view(),name='product_details')
]