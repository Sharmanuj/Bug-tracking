from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from bug_reports.models import BugReport
from bug_reports.forms import BugCreateForm


class BugCreateView(LoginRequiredMixin, CreateView):

    model = BugReport
    form_class = BugCreateForm
    success_url = reverse_lazy('index')
    template_name = 'bug_reports/new_bug_report.html'


class BugUpdateView(LoginRequiredMixin, UpdateView):

    model = BugReport
    fields = '__all__'
    template_name = 'bug_reports/edit_bug_report.html'
    pk_url_kwarg = 'bug_pk'
    context_object_name = 'bugreport'
    success_url = reverse_lazy('index')


class BugListView(LoginRequiredMixin, ListView):
    model = BugReport
    context_object_name = 'bug_reports'
    template_name = 'bug_reports/bug_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BugListView, self).get_context_data(**kwargs)
        project_id = self.kwargs.get('project_pk')
        data = []
        for bug in BugReport.objects.filter(project_id=project_id):
            data.append({
                'title': bug.title,
                'description': bug.description,
                'id': bug.id,
                'severity': bug.severity,
                'status': bug.status,
                'project_id': project_id
            })

        context['bug_reports'] = data
        return context


class BugDeleteView(LoginRequiredMixin, DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_pk'
    context_object_name = 'bugreport'
    template_name = 'bug_reports/delete_bug_report.html'
    success_url = reverse_lazy('index')
