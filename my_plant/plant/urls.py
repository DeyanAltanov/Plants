from django.urls import path

from my_plant.plant.views import home, create_profile, catalogue, create_plant, plant_details, edit_plant, delete_plant, \
    profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', home, name='home'),
    path('profile/create/', create_profile, name='create profile'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>', plant_details, name='plant details'),
    path('edit/<int:pk>', edit_plant, name='edit plant'),
    path('delete/<int:pk>', delete_plant, name='delete plant'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]