from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils import timezone
from ych_admin.models import *
import os
from django.conf import settings

# from django.http.request import QueryDict

# Client Side
def ych_home(request):
    return redirect('/')

def ych_base(request):
    homeData = Home.objects.all()
    menus = Menu.objects.all()
    homeButtons = HomeButton.objects.all()
    today = timezone.now()
    today = today.strftime("%d %b %Y")

    # Services
    services = Service.objects.all()

    # About-us
    aboutus = About.objects.all()

    # Contact-us
    contactus = Contact.objects.all()
    context = {
        "homeData": homeData, 
        "menus":menus, 
        "homeButtons": homeButtons,
        "services": services,
        "aboutus": aboutus,
        "contactus":contactus,
        "today": today,
    }
    
    return render(request, 'ych/data.html', context )

def loginPage(request):
    title = 'Good Job!'
    msg = ''
    icon = 'success'
    form = request.POST or None
    if form != None:
        try:
            usersData = Users.objects.get(user_email=request.POST['email'])
    
            if pbkdf2_sha256.verify(request.POST['pwd'],usersData.user_pass):
                msg = "Loggedin Successfully!"
                request.session['id'] = usersData.id
                return render(request, 'ych_admin/dashboard.html', {"msg":msg, "icon":icon,"title":title})
            else:
                title = 'Try again!'
                msg = "Password does not match!"
                icon= "warning"
        
        except:

            title = 'Try again!'
            msg = "Email and Password does not match, Please Register!"
            icon= "warning"
                      

    menus = Menu.objects.all()
    context = { 
        "menus":menus,
        "msg":msg,
        "icon":icon,
        "title":title}
    return render(request, 'ych/login.html', context)

def registerPage(request):

    title = 'Good Job!'
    msg = ''
    icon = 'success'
    form = request.POST or None
    if form != None:
        try:
            checkUsers = Users.objects.get(user_email = request.POST['email'])
            title = 'Try again!'
            msg = "Email already exist!"
            icon= "warning"
            
        except:
            
            obj = Users.objects.create(
                user_name = request.POST['uname'],
                user_email = request.POST['email'],
                user_pass = pbkdf2_sha256.hash(request.POST['pwd'])
            )
            obj.save()
            
            msg = "You are Registered, Please Login."
       
            return render(request, 'ych/login.html', {"msg":msg, "icon":icon,"title":title})

    menus = Menu.objects.all()
    context = { 
        "menus":menus,
        "msg":msg,
        "icon":icon,
        "title":title}
    return render(request, 'ych/register.html', context)


# Admin Side
def admin_dashboard(request):

    try:
        user_id = request.session['id']
        user_dtl = Users.objects.get(id=user_id)
        return render(request,'ych_admin/dashboard.html',{'user_dtl':user_dtl})
    except:
        return redirect('/login')
    # return render(request, 'ych_admin/base.html')


def logoutPage(request):
    del request.session['id']
    return redirect('/login')

# Admin Menu
def admin_menu(request):
    try:
        id = request.session['id']
    
        title = 'Good Job!'
        msg = ''
        icon = 'success'
        form = request.POST or None
        if form != None:
            obj = Menu.objects.create(
                menu = request.POST['menu'],
            )
            obj.save()
            msg = "Record Inserted."
        
        menus = Menu.objects.all()
        return render(request, 'ych_admin/menu.html', {"menus": menus, "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def edit_menu(request, menu_id):
    try:
        id = request.session['id']
    
        obj = Menu.objects.get(id=menu_id)
        return render(request, 'ych_admin/menu-edit.html', {"m": obj})
    except:
        return redirect('/login')

def update_menu(request):
    try:
        id = request.session['id']

        if request.method == "GET":

            obj = Menu.objects.get(id=request.GET['mid'])
            obj.menu = request.GET['updateval']
            obj.save()
        return HttpResponse()
    except:
        return redirect('/login')
    

def delete_menu(request, menu_id):
    try:
        id = request.session['id']

        obj = Menu.objects.get(id=menu_id)
        obj.delete()
        return redirect('/menu')
    except:
        return redirect('/login')

# Admin Home Page
def adminHomepage(request):
    try:
        id = request.session['id']

        title = 'Good Job!'
        msg = ''
        icon = 'success'
        form = request.POST or None
        if form != None:
            obj = Home.objects.create(
                home_title = request.POST['home_title'],
                home_content = request.POST['home_content']
            )
            obj.save()
            msg = "Record Inserted."

        home_data = Home.objects.all()
        return render(request, 'ych_admin/home.html', {"home_data": home_data, "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def editHomepage(request, home_id):
    try:
        id = request.session['id']

        obj = Home.objects.get(id = home_id)
        return render(request, 'ych_admin/home-edit.html', {"home_data": obj} )
    except:
        return redirect('/login')

def updateHomepage(request, home_id):
    try:
        id = request.session['id']

        obj = Home.objects.get(id = home_id)
        obj.home_title = request.POST['home_title']
        obj.home_content = request.POST['home_content']
        obj.save()
        
        title = 'Good Job!'
        msg = 'Record Updated Successfully.'
        icon = 'success'
        
        return render(request, 'ych_admin/home.html', { "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def deleteHomepage(request, home_id):
    try:
        id = request.session['id']

        obj = Home.objects.get(id = home_id)
        obj.delete()
        return redirect('/home-page')
    except:
        return redirect('/login')

# Admin Services
def adminServices(request):
    try:
        id = request.session['id']

        title = 'Good Job!'
        msg = ''
        icon = 'success'
        form = request.POST or None
        if form != None:
            obj = Service.objects.create(
                service_title = request.POST['service_title'],
                service_content = request.POST['service_content'],
                service_i_tag = request.POST['service_i_tag']
            )
            obj.save()
            msg = "Record Inserted."
            
        services = Service.objects.all()
        return render(request, 'ych_admin/services.html', {"services":services, "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def editService(request, service_id):
    try:
        id = request.session['id']

        obj = Service.objects.get(id = service_id)
        return render(request, 'ych_admin/services-edit.html', {"service":obj})
    except:
        return redirect('/login')

def updateService(request, service_id):
    try:
        id = request.session['id']

        obj = Service.objects.get(id = service_id)
        obj.service_title = request.POST['service_title']
        obj.service_content = request.POST['service_content']
        obj.service_i_tag = request.POST['service_i_tag']
        obj.save()

        title = 'Good Job!'
        msg = 'Record Updated Successfully.'
        icon = 'success'
        
        return render(request, 'ych_admin/services.html', { "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def deleteService(request, service_id):
    try:
        id = request.session['id']

        obj = Service.objects.get(id = service_id)
        obj.delete()
        return redirect('/services')
    except:
        return redirect('/login')

# Gallery
def galleries(request):
    # try:
    id = request.session['id']

    title = 'Good Job!'
    msg = ''
    icon = 'success'
    form = request.POST or None
    if form != None:
        obj = Gallery.objects.create(
            img = request.FILES['image'],
        )
        obj.save()
        msg = "Image Inserted."

    img_data = Gallery.objects.all()
    return render(request, 'ych_admin/gallery.html', {"img_data": img_data, "msg":msg,"icon":icon,"title":title})

    # except Exception as e:
    #     print(e)
    #     return redirect('/login')

def deleteImg(request, img_id):
    try:
        id = request.session['id']

        obj = Gallery.objects.get(id = img_id)
        
        file = os.path.join(settings.MEDIA_ROOT, str(obj.img))
        newFile = file.replace('\\','/')
        
        os.remove(newFile)
        obj.delete()
        return redirect('/gallery')
    except:
        return redirect('/login')

# About-Us
def adminAboutus(request):
    try:
        id = request.session['id']

        title = 'Good Job!'
        msg = ''
        icon = 'success'
        form = request.POST or None
        # if form != None:
        #     obj = About.objects.create(
        #         about_content = request.POST['about_content']
        #     )
        #     obj.save()
        #     msg = "Record Inserted."

        abouts = About.objects.all()
        return render(request, 'ych_admin/about-us.html', {"abouts":abouts, "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def editAboutus(request, aboutus_id):
    try:
        id = request.session['id']
        
        obj = About.objects.get(id = aboutus_id)
        return render(request, 'ych_admin/about-us-edit.html', {"about":obj})
    except:
        return redirect('/login')

def updateAboutus(request, aboutus_id):
    try:
        id = request.session['id']

        obj = About.objects.get(id = aboutus_id)
        obj.about_content = request.POST['about_content']
        obj.save()
        title = 'Good Job!'
        msg = 'Record Updated Successfully.'
        icon = 'success'
        
        return render(request, 'ych_admin/about-us.html', { "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def deleteAboutus(request, aboutus_id):
    try:
        id = request.session['id']

        obj = About.objects.get(id = aboutus_id)
        obj.delete()
        return redirect('/about-us')
    except:
        return redirect('/login')

# Contact-Us
def adminContactus(request):
    try:
        id = request.session['id']

        title = 'Good Job!'
        msg = ''
        icon = 'success'
        form = request.POST or None
        if form != None:
            try:
                contactNum = Contact.objects.get(contact_num = request.POST['contact_num'])
                title = 'Try again!'
                msg = "Contact number already exist!"
                icon= "warning"
                
            except:
                
                obj = Contact.objects.create(
                    contact_num = request.POST['contact_num'],
                    contact_title = request.POST['contact_title'],
                    contact_address = request.POST['contact_address']
                )
                obj.save()
                
                msg = "Record Inserted."
                
        contactus = Contact.objects.all()
        return render(request, 'ych_admin/contact-us.html', {"contactus": contactus, "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def editContactus(request, contact_id):
    try:
        id = request.session['id']

        obj = Contact.objects.get(id = contact_id)
        return render(request, 'ych_admin/edit-contact-us.html', {"contact": obj})
    except:
        return redirect('/login')

def updateContactus(request, contact_id):
    try:
        id = request.session['id']
        try:
            contactNum = Contact.objects.get(contact_num = request.POST['contact_num'])
            title = 'Try again!'
            msg = "Contact number already exist!"
            icon= "warning"
            
        except:
            
            obj = Contact.objects.get(id = contact_id)
            obj.contact_num = request.POST['contact_num']
            obj.contact_title = request.POST['contact_title']
            obj.contact_address = request.POST['contact_address']
            obj.save()
            
            msg = 'Record Updated Successfully.'
        return render(request, 'ych_admin/contact-us.html', { "msg":msg,"icon":icon,"title":title})
    except:
        return redirect('/login')

def deleteContactus(request, contact_id):
    try:
        id = request.session['id']

        obj = Contact.objects.get(id = contact_id)
        obj.delete()
        
        return redirect('/contact-us')
    except:
        return redirect('/login')