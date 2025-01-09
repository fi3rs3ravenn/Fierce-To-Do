from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'full_name']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username' , 'nickname' , 'email' , 'avatar' , 'age']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar' , 'nickname' , 'bio' , 'streak']
        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control','rows':3}),
        }


