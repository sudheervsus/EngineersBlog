from django import forms
from accounts.models import User


class UserSignUPForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email','password','first_name','last_name']
        labels = {
        'username':'User Name',
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

    def save(self):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        return user
