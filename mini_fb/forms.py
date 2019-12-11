# <!-- quotes/forms.py -->

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to add new quotes to teh database.'''

    class Meta:
        '''associate this form w Profile model '''
        model = Profile
        fields = ['first_name','last_name','home_town','email','prof_url'] #which fields from model 

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a profile to the database.'''

    class Meta: 
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['home_town','email','prof_url'] #which fields from model should we use

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to update a status message to the database.'''
    image = forms.ImageField(required = False)
    class Meta: 
        '''associate this form with the statusMessage model.'''
        model = StatusMessage
        fields = ['message','image'] #whichfields
        
