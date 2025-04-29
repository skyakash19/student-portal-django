from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

# ✅ Main Signup Form with both User and Student fields
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'profile_photo']


# ✅ Optional: Profile update form (if needed)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


# ✅ Optional: Student-only form (can be removed if unused)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['bio', 'profile_photo']
