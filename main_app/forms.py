from django import forms
from django.forms.widgets import DateTimeInput
from django import ModelForm
from main_app.models import, Project, Task, Comment

class ProjectForm(forms.ModelForm):
  due_date = forms.DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = Project
    fields = [...]

class TaskForm(forms.ModelForm):
  created_date = forms. DateTimeField(widget=CustomDateTimeInput()),
  due_date = forms.DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = Task
    fields = [...]

class CommentForm(forms.ModelForm):
  created_date = forms.DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = Comment
    fields = [...]
