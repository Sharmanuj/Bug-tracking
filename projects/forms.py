from django import forms
from projects.models import Project


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
