from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # This view class is protected from unauthorized access.
    path('me/', login_required(ResourcesView.as_view()), name='resources'),
    
    # User authentication can be made mandatory in other ways: 
    # Creating logic in each view function or using decorators in each view function or 
    # creating custom authentication middleware for large apps. 
]