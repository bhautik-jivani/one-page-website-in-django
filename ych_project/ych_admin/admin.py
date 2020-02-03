from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Home)
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_pass')
    search_fields = ['user_name', 'user_email']
    ordering = ['user_name', 'user_email']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('home_title', 'home_content')
    search_fields = ['home_title']
    ordering = ['home_title']

@admin.register(HomeButton)
class HomeButtonAdmin(admin.ModelAdmin):
    list_display = ['home_btn', 'home_btn_class', 'home_btn_link']
    search_fileds = ['home_btn', 'home_btn_class']
    ordering = ['home_btn', 'home_btn_class']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu']
    search_fields = ['menu']
    ordering = ['menu']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_i_tag', 'service_content']
    search_fields = ['service_title', 'service_i_tag']
    ordering = ['service_title', 'service_i_tag']

admin.site.register(About)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_num', 'contact_title','contact_address']
    search_fields = ['contact_num', 'contact_title', 'contact_address']
    ordering = ['contact_num', 'contact_title']

@admin.register(Gallery)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['img']
    search_fields = ['img']