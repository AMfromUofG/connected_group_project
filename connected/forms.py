from django import forms
from django.contrib.auth.models import User
from connected.models import Event, Category, UserProfile, MAX_LENGTH_NAME

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=MAX_LENGTH_NAME, help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Category
        fields = ('name', )
        
class EventForm(forms.ModelForm):
    title = forms.CharField(max_length=MAX_LENGTH_NAME,
                            help_text="Please enter the title of the page.")
    date = forms.CharField()
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    signups = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Event
        exclude = ('category', )

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
            
        return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture', )