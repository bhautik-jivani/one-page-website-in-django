from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'ych_admin'

urlpatterns = [
    path('', ych_base),
    path('home/', ych_home),

    path('dashboard/', admin_dashboard),
    path('login/', loginPage),
    path('register/', registerPage),
    path('logout/', logoutPage),

    # Menu
    path('menu/', admin_menu),
    path('edit-menu/<int:menu_id>/', edit_menu),
    path('update-menu/', update_menu),
    path('delete-menu/<int:menu_id>/', delete_menu),

    # Home-page
    path('home-page/', adminHomepage),
    path('edit-home-page/<int:home_id>/', editHomepage),
    path('update-home-page/<int:home_id>/', updateHomepage),
    path('delete-home-page/<int:home_id>/', deleteHomepage),

    # Services
    path('services/', adminServices),
    path('edit-service/<int:service_id>/', editService),
    path('update-service/<int:service_id>/', updateService),
    path('delete-service/<int:service_id>/', deleteService),

    # Gallery
    path('gallery/', galleries),
    path('delete-gallery/<int:img_id>/', deleteImg),

    # Abous-Us
    path('about-us/', adminAboutus),
    path('edit-aboutus/<int:aboutus_id>/', editAboutus),
    path('update-aboutus/<int:aboutus_id>/', updateAboutus),
    path('delete-aboutus/<int:aboutus_id>/', deleteAboutus),

    # Contact-Us
    path('contact-us/', adminContactus),
    path('edit-contactus/<int:contact_id>/', editContactus),
    path('update-contactus/<int:contact_id>/', updateContactus),
    path('delete-contactus/<int:contact_id>/', deleteContactus),
] 