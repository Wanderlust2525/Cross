from django import forms


class LoginForm(forms.Form):

    username =forms.CharField(label = 'Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'create-form', 'placeholder': 'Имя пользователя'}))
    
    password =forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={
        'class': 'create-form', 'placeholder': 'Password'}))

    
