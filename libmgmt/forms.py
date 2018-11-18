from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=10,\
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),\
        error_messages={'required': 'Username is required', 'max_length': 'Username cannot be more than 10'})
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),\
        error_messages={'required': 'Password is required'})

class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=10,\
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),\
        error_messages={'required': 'Username is required', 'max_length': 'Username cannot be more than 10'})
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),\
        error_messages={'required': 'Password is required'})
    country = forms.ChoiceField(label='Country', choices=(('IN','India'),('CR', 'Costa Rica')))
    gender = forms.ChoiceField(widget=forms.RadioSelect, label='Gender', choices=(('M', 'Male'),('F', 'Female')))
    dob = forms.DateField(label='DOB',\
     widget=forms.DateInput(attrs={'class':'datepicker'}))

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        tokens = username.split(' ')
        if len(tokens) > 1:
            raise forms.ValidationError('Username should not have spaces')
        return username
