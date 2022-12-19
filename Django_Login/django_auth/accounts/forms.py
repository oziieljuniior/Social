from django import forms
from .models import System_Post
from django.contrib.auth.forms import UserCreationForm

class SystemForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={"placeholder": "Post something ...",
                                      "class": "textarea is-success is-medium",}
                           ),
                           label = "",)

    class Meta:
        model = System_Post
        exclude = ("user", )

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)