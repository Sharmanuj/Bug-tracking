from django.urls import path
from projects.views import ProjectCreateView, ProjectUpdateView, ProjectListView, ProjectDeleteView

urlpatterns = [
    path('projectcreate/', ProjectCreateView.as_view(), name='projectcreate'),
    path('projectupdate/<int:project_pk>/', ProjectUpdateView.as_view(), name='projectupdate'),
    path('projectdelete/<int:project_pk>/', ProjectDeleteView.as_view(), name='projectdelete'),
    path('projectlist/', ProjectListView.as_view(), name='projectlist'),
]
