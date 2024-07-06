from . models import User
from food.models import ContactUs
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

@login_required(login_url='login')
def Profile(request):
     return render(request,'user/profile.html')


def Register(request):

    if request.method == "POST":
            data = request.POST

            fn = data.get('fn')
            ln = data.get('ln')
            un = data.get('un')
            email = data.get('email')
            mobile = data.get('mobile')
            address = data.get('address')
            password = data.get('password')
            cpassword = data.get('cpassword')
            
            if User.objects.filter(username=un).exists():
                messages.error(request, 'User Name already exist.')
                return render(request, 'user/register.html')
            
            if not all([fn, ln, un, email, mobile, address]):
                messages.error(request, 'All Fields Required')
                return render(request, 'user/register.html')    

            if password != cpassword:
                messages.error(request, 'Passwords do not match. Please try again.')
                return render(request, 'user/register.html')
            
            if 'image' in request.FILES:
                profile = request.FILES['image']
                data = User.objects.create_user(username=un,password = password,email=email,address=address,mobile=mobile,first_name=fn,last_name=ln,profile=profile)
                data.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
            
    return render(request,'user/register.html')


def Login(request):
     
    if request.method == "POST":
         data = request.POST
         username = data.get('username')
         password = data.get('password')

         user = authenticate(request, username = username, password = password )
         if user is not None :
              login(request,user)
              messages.success(request, 'Successfully signed in!')
              return redirect('home')  # Redirect to a home page or dashboard
         else:
              messages.error(request, 'Please try again.')
              return render(request, 'user/login.html')
              
    return render(request,'user/login.html')

def Logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login') 

@login_required(login_url='login')
def UpdateProfile(request):

    if request.method == "POST":
        data = request.POST

        fn = data.get('fn')
        ln = data.get('ln')
        un = data.get('un')
        email = data.get('email')
        mobile = data.get('mobile')
        address = data.get('address')
        password = data.get('password')

        if request.user.is_authenticated:
            # Update existing user information
            user = request.user
            user.first_name = fn
            user.last_name = ln
            user.username = un
            user.email = email
            user.mobile = mobile
            user.address = address

            if 'image' in request.FILES:
                user.profile = request.FILES['image']

            user.set_password(password)
            user.save()
            messages.success(request, 'Account updated successfully!')
            return redirect('Profile')  # Redirect to a pro

    return render(request,'user/update.html')

def Contact(request):
    if request.method == "POST":
        data = request.POST
        db = ContactUs()
        db.customer = request.user
        db.name = data.get('name')
        db.message = data.get('message')
        db.email = data.get('email')
        if not (db.name and  db.message and db.email):
            error_message = "All fields are required."
            return render(request, 'about.html', {'error_message': error_message, 'data': data})

        db.save()

        subject = "new Query "
        from_email = 'info.demodjango@gmail.com'
        recipient_list = ['info.demodjango@gmail.com'] 
        
        context = {
            'name': db.name,
            'email': db.email,
            'subject':subject,
            'message': db.message,
        }
        text_content = f"Name: {db.name}\nEmail: {db.email}\nMessage: {db.message}\nSubject:{subject}"
        html_content = render_to_string('contact_email.html', context)

        # Send email
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()

        messages.success(request, 'This data has been sent to the admin.')
       
        return redirect('about')
    return render(request,'about.html')



   