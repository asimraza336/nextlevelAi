from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=False)
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    # last_name = forms.CharField(
    #     max_length=30, required=True, help_text='Required')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'phone_number', 'company', 'job_title','password1', 'password2', )
        
    # def clean_username(self):
    #     # here
    #     print('----------------------------------------------------------------')
    #     print(self.cleaned_data)
    #     data = self.cleaned_data['email']
    #     print(data)
    #     return data
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['job_title'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your full name here'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email here'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your Phone Number here'
        self.fields['company'].widget.attrs['placeholder'] = 'Enter your Company Name here'
        self.fields['job_title'].widget.attrs['placeholder'] = 'Enter your Job Title here'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password here'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password here'
        
        
        


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=300, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)
    
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your Password'