from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.generic import TemplateView
from .models import MenuItem,Restaurant,Order,OrderItem
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from useraccount.models import Clients  
from django.db.models import Q
from django.core.paginator import Paginator


class About(TemplateView):
    template_name = 'about.html'

class Book(TemplateView):
    template_name = 'book.html'



class Login(TemplateView):
    template_name = 'user/login.html'



def Index(request):
    search =request.GET.get("search","")
    resturent = Restaurant.objects.all()
    menu = MenuItem.objects.all()
    carousel = MenuItem.objects.all()[:3]
    clints = Clients.objects.filter(status=True)
    menu = {}
    for rest in resturent:
        if search:
            Menu = MenuItem.objects.filter(restaurant=rest).filter(Q(name__icontains=search) | Q(description__icontains=search)).order_by('created_at')[:10]
        else:
            Menu = MenuItem.objects.filter(restaurant=rest).order_by('created_at')[:10]
        menu[rest.id] = Menu[:4]

    context = {
         'data':resturent,
         'menu':menu ,
         'clints':clints,
         'carousel':carousel,
    }
    return render(request,'index.html',context)


def MenuItems(request):
    search =request.GET.get("search","")
    resturent = Restaurant.objects.all()
    menu = MenuItem.objects.all()
    menu = {}
    for rest in resturent:
        if search:
            Menu = MenuItem.objects.filter(restaurant=rest).filter(Q(name__icontains=search) | Q(description__icontains=search))[:10]
        else:
            Menu = MenuItem.objects.filter(restaurant=rest)[:10]
        menu[rest.id] = Menu[:10]
    return render(request,'menu.html',{'data':resturent,'menu':menu})


def Detail(request,id):   
    food = get_object_or_404(MenuItem, id=id)
    return render(request,'details.html',{'food':food})



@login_required(login_url='login')
def AddOrder(request,order_id):
    menu_item = get_object_or_404(MenuItem,id = order_id)
    order, created = Order.objects.get_or_create(customer=request.user)
    order_item, created = OrderItem.objects.get_or_create(order =order,menu_item = menu_item,defaults={'quantity': 1, 'price': menu_item.price})

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('order')


@login_required(login_url='login')
def OrderView(request):
    order = get_object_or_404(Order, customer=request.user)
    order_item = OrderItem.objects.filter(order=order)  # Retrieve all items associated with the order
    for item in order_item:
        item.total_price = item.price * item.quantity
    total_price = sum(item.price * item.quantity for item in order_item)
    return render(request, 'order_list.html', {'order': order, 'order_items': order_item,'total_price':total_price})

@login_required
def remove_Order(request, order_id):
    cart_item = get_object_or_404(OrderItem, id=order_id)
    cart_item.delete()
    return redirect('order')

@login_required(login_url='login')
def proceed_to_payment(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, customer=request.user)
        order_items = OrderItem.objects.filter(order=order)
        total_price = sum(item.price * item.quantity for item in order_items)

        email_subject = 'Order Confirmation'
        email_body = render_to_string('order_email.html', {
            'order': order,
            'order_items': order_items,
            'total_price': total_price
        })
        
       
        if order_items.exists():
            # Send email
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[request.user.email]
            )
            email.content_subtype = 'html'  # Important to set the email content type to HTML
            email.send()

        
            order.status = 'Paid'  
            order.save()
            OrderItem.objects.filter(order=order).delete()
            return HttpResponse("Payment successful! Your order has been processed.")
        else:
            return redirect('order')
        
    else:
        return redirect('order')