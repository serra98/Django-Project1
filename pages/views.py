from django.shortcuts import render
from django.http import HttpResponse # create a response to a URL request 
from django.views.generic import TemplateView #base class for a generic view 


# Create your views here.

class HomePageView(TemplateView):
    '''Inherit from the generic TemplateView to use an external HTML template '''
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    '''Inherit from the generic TemplateView to use an external HTML template '''
    template_name = 'pages/about.html'
    
#def homePageView(request):
   # ''' This function will respond to an HTTP request and return an HttpRequest object.'''

  

  #  s = '''
#<html>
#<head> 
 #   <title>Hello,world!</title>
#</head>
#<body>
#<h1>Hello,world! </h1>
#Welcome to our first Django web application! 
#<p> 

#</body>
#</html>
  #  '''
 #   return HttpResponse(s)