from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from projects.models import Project
from projects.forms import ProjectCreateForm
from bug_reports.constants import Status


class ProjectCreateView(LoginRequiredMixin, CreateView):

    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy('index')
    template_name = 'projects/new_project.html'


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    model = Project
    fields = '__all__'
    template_name = 'projects/edit_project.html'
    pk_url_kwarg = 'project_pk'
    context_object_name = 'project'
    success_url = reverse_lazy('index')


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        data = []
        for project in Project.objects.all():
            data.append({
                'title': project.title,
                'description': project.description,
                'users': str(list(project.users.all().values_list('username', flat=True))),
                'start_date': project.start_date,
                'id': project.id,
                'total_bugs': project.bug.all().count(),
                'in_progress_bugs': project.bug.filter(status=Status.INPROGRESS).count(),
                'resolved_bugs': project.bug.filter(status=Status.RESOLVED).count()
            })

        context['projects'] = data
        return context


class ProjectShowListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/project_show_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectShowListView, self).get_context_data(**kwargs)
        data = []
        for project in Project.objects.all():
            data.append({
                'title': project.title,
                'description': project.description,
                'users': str(list(project.users.all().values_list('username', flat=True))),
                'start_date': project.start_date,
                'id': project.id,
                'total_bugs': project.bug.all().count(),
                'in_progress_bugs': project.bug.filter(status=Status.INPROGRESS).count(),
                'resolved_bugs': project.bug.filter(status=Status.RESOLVED).count()
            })

        context['projects'] = data
        return context


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    pk_url_kwarg = 'project_pk'
    context_object_name = 'project'
    template_name = 'projects/delete_project.html'
    success_url = reverse_lazy('index')
