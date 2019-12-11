from django.shortcuts import render

# Create your views here.
from .models import Profile , StatusMessage
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView

from .forms import CreateProfileForm , UpdateProfileForm , CreateStatusMessageForm 
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView):
    '''create a subclass of listview to display all mini_fb'''

    model = Profile #retrieve obejcts of type mini_fb from database 
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_mini_fb_list'

class ShowProfilePageView(DetailView):
    '''show the detail for one mini_fb'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context
    
    
class ShowNewsFeedView(DetailView):
    '''do everything we want withuot overriding any method. '''

    model = Profile 
    template_name = 'mini_fb/show_news_feed.html'
    context_object_name = 'profile'


class ShowPossibleFriendsView(DetailView):
    '''will do everything we want, without overriding any methods.'''
    model = Profile 
    template_name = 'mini_fb/show_possible_friends.html' 
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    '''A view to create a new quote and save it to tjhe database'''

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(CreateView):
    '''A view to update a new quote and save it to tjhe database'''

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()

def create_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    #read request data into AddImageForm object 
    form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']
        #image = request.POST['image']

        # save the new status message object to the database
        if form.is_valid():

            sm = form.save(commit = False)
            sm.profile = profile
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class DeleteStatusMessageView(DeleteView):
    ''' A view to delete a quote and remove it from a database.'''

    template_name = "mini_fb/delete_status_form.html"
    queryset = Profile.objects.all()
    #success_url = "" #what to do after deleting 

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        #find status message object that we re trying to deleete and save it to variable
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        profile = Profile.objects.get(pk=self.kwargs['profile_pk'])

        context['status'] = st_msg
        context['profile'] = profile

        return context

    def get_object(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        #success_url = "profile/<int:pk>" #what to do after deleting 

        # find the StatusMessage object, and return it
        smg = StatusMessage.objects.filter(profile=profile_pk, pk = status_pk)
        return smg

    def get_success_url(self):
        ''' return a the url to which we should be directed after the dleete.'''

        #read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']

        return reverse('show_profile_page', kwargs={'pk':profile_pk})


def add_friend(request,profile_pk,friend_pk):
    ''' process the add_friend request, to add a friend for a given profile. '''
    
    # find the profile object which is adding the friend and store it into variable 
    profile = Profile.objects.get(pk=profile_pk)

    #find the profile object of the friend to add, and store it into another variable 
    friend = Profile.objects.get(pk=friend_pk)

    #add that friend's {rofile into the profile.friends object using the method add.
    profile.friends.add(friend)

    #return / save the profile object 
    return redirect(reverse ('show_profile_page', kwargs={'pk':profile_pk}))

