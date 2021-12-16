from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['poster', 'timestamp', 'reviews', 'usability', 'content', 'design', 'rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['poster','project', 'upload_date']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['poster', 'project', 'average']

class RatingForm(forms.ModelForm):
    class Meta:
        model = ProjectVote
        fields = ['design', 'usability', 'content']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']