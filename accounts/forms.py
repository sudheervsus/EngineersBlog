from django import forms
from accounts.models import User


class UserSignUPForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email','password','first_name','last_name']
        labels = {
        'username':'Display Name',
        'first_name': "First Name",
        'last_name':'Last Name',
        }
        widgets = {
            'username': forms.TextInput(attrs = { 'class':'form-control' }),
            'email': forms.EmailInput(attrs = { 'class':'form-control' }),
            'password': forms.PasswordInput(attrs = { 'class':'form-control' }),
            # 'password2': forms.PasswordInput(attrs = { 'class':'form-control' }),
            'first_name': forms.TextInput(attrs = { 'class':'form-control' }),
            'last_name': forms.TextInput(attrs = { 'class':'form-control' }),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'Display Name'
    #     self.fields['email'].label = 'Email Address'
    #     self.fields['first_name'].label = 'First Name'
    #     self.fields['last_name'].label = 'Last Name'
