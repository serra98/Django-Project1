# mini_fb/urls.py

from django.urls import path 
from .views import ShowAllProfilesView , ShowProfilePageView , CreateProfileView , UpdateProfileView ,create_status_message , DeleteStatusMessageView , ShowNewsFeedView ,ShowPossibleFriendsView , add_friend #our view class definition

urlpatterns = [
    path('',ShowAllProfilesView.as_view(), name='show_all_profiles'), #generic class - base view 
    path('profile/<int:pk>',ShowProfilePageView.as_view(), name='show_profile_page' ),#show one profile
    path('profile/<int:pk>/update',UpdateProfileView.as_view(), name = 'update_profile'),
    path('profile/<int:pk>/post_status',create_status_message,name = 'post_status'),
    path('create_profile',CreateProfileView.as_view(),name='create_profile'),
    path('profile/<int:pk>/news_feed',ShowNewsFeedView.as_view(), name = 'news_feed'),
    path('profile/<int:pk>/show_possible_friends',ShowPossibleFriendsView.as_view(),name = 'show_possible_friends'),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>',add_friend,name ='add_friend'),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>',DeleteStatusMessageView.as_view(),name = 'delete_status')
] 