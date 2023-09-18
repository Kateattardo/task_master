from django.forms.widgets import DateTimeInput
from django import ModelForm
from main_app.models import, Project, Task, Comment

class ProjectForm(forms.ModelForm):
  date_field_name = forms.DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = project
    fields = [...]

class TaskForm(forms.modelForm):
  date_field_name = forms. DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = Task
    fields = [...]

class CommentForm(forms.ModelForm):
  date_field_name = forms.DateTimeField(widget=CustomDateTimeInput())

  class Meta:
    model = Comment
    fields = [...]
