from django import forms
from bug_reports.models import BugReport


class BugCreateForm(forms.ModelForm):

    class Meta:
        model = BugReport
        fields = '__all__'
