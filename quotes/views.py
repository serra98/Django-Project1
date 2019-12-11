from django.shortcuts import render

# Create your views here.
from .models import Quote , Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse 
from .forms import CreateQuoteForm , UpdateQuoteForm , AddImageForm
from django.shortcuts import redirect 
import random

class HomePageView(ListView):
    '''create a subclass of ListView to display all quotes.'''

    model = Quote #retrieve objects of type Quote from database 
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    '''show one quote'''

    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    ''' show one quote selected at random.'''
    model = Quote 
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    #pick one quote at random 
    def get_object(self):
        '''return a single instance of a quote object, selected at random.'''
        # get all quotes 
        all_quotes = Quote.objects.all() 
        # pick one, at random 
        r = random.randint(0,len(all_quotes) -1)
        q = all_quotes[r]
        return q


class PersonPageView(DetailView):
    '''show all quotes and all images for one person.'''

    model = Person 
    template_name = 'quotes/person.html'
   # context_object_name = 'person'

    def get_context_data(self, **kwargs):
        '''return a dictionary with context data for this template to use.'''
        
        # get the default context data: 
        # this will include the person record for this page view 
        context = super(PersonPageView, self).get_context_data(**kwargs)

        #create add image form: 
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form 

        #return the context dictionary:
        return context


class CreateQuoteView(CreateView):
    '''A view to create a new quote and save it to tjhe database'''

    form_class = CreateQuoteForm
    template_name = 'quotes/create_quote.html'

    
class UpdateQuoteView(CreateView):
    '''A view to update a new quote and save it to tjhe database'''

    form_class = UpdateQuoteForm
    template_name = 'quotes/update_quote.html'
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    ''' A view to delete a quote and remove it from a database.'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    success_url = "../../all" #what to do after deleting 

    def get_success_url(self):
        ''' return a the url to which we should be directed after the dleete.'''

        # get the pk for this quote 
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()

        #find the person associated with the quote 
        person = quote.person 
        return reverse('person', kwargs={'pk':person.pk})

def add_image(request,pk):
    '''A custom view function to handle the submission of an image upload.'''

    #find the person for whom who are submitting the iamge 
    person = Person.objects.get(pk=pk)

    #read request data into AddImageForm object 
    form = AddImageForm(request.POST or None, request.FILES or None)
    #check if the form is valid, save object to database 
    if form.is_valid():
        image = form.save(commit = False) #create the image object, but not save 
        image.person = person 
        image.save() #story to the database
    else: 
        print("Error: the form was not valid.")

    #redirect to a new URL , display person page 
    url = reverse('person', kwargs = {'pk':pk})
    return redirect(url)
