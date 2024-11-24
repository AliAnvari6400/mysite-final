from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from accounts.models import CustomUser


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ResetForm(forms.Form):
    email = forms.EmailField()
    
    
class ChangeForm(forms.Form):
    password1 = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)