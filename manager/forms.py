from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker, Task


class WorkerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
        )


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )
