from django.shortcuts import render

# Create your views here.
def registrartion_user(request) :
    return render(request, 'registerPage.html')

def login_user(request) :
    return render(request, 'loginPage.html')

def logout_user(request) :
    return render(request, 'logoutPage.html')

def delete_user(request) :
    return render(request, 'deletePage.html')

def profile_page(request) :
    return render(request, 'profilePage.html')

def edit_profile_page(request) :
    return render(request, 'editProfilePage.html')

