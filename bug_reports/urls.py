from django.urls import path
from bug_reports.views import BugCreateView, BugUpdateView, BugListView, BugDeleteView

urlpatterns = [
    path('bugreportcreate/', BugCreateView.as_view(), name='bugreportcreate'),
    path('bugreportupdate/<int:bug_pk>/', BugUpdateView.as_view(), name='bugreportupdate'),
    path('bugreportlist/<int:project_pk>/', BugListView.as_view(), name='bugreportlist'),
    path('bugreportdelete/<int:bug_pk>/', BugDeleteView.as_view(), name='bugreportdelete'),
]
