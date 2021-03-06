from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model, 
    login,
    logout,
    )
from .models import Profile

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("User doesn't exist")

            if not user.is_active:
                raise forms.ValidationError('Inactive user')

            return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already existed")

        return email

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        label='Biography',
        widget=forms.Textarea(
            attrs={'placeholder':'Something about me'}  
        ), 
        required=False,
    )
    class Meta:
        model = Profile
        fields = [
            'image',
            'bio', 
        ]
