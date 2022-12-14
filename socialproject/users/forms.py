from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('photo',)



class LoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

#ModelForm: it works on a particular model, in this case the built-in User model
class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #To confirm password, we require password2:
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)
   
#Meta class allows us to add info about the form itself
    class Meta:
        model = User
        fields={'first_name','username', 'email'}

    #Check if passwords match and display message:
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']