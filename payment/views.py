from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib import messages
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from storefront.models import Product, Profile
import datetime
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
# Create your views here.


def process_order(request):
	if request.POST:
		cart=Cart(request)
		cart_products=cart.get_prods
		quantities=cart.get_quants
		totals= cart.cart_total()

		payment_form = PaymentForm(request.POST or None) 
		shipping_info=request.session.get('shipping_info')
		
		full_name=shipping_info['shipping_full_name']
		email=shipping_info['shipping_email']
		amount_paid=totals
		user=request.user
		shipping_address= f"{shipping_info['shipping_address1']}\n{shipping_info['shipping_address2']}\n{shipping_info['shipping_city']}\n{shipping_info['shipping_state']}\n{shipping_info['shipping_zipcode']}\n{shipping_info['shipping_country']}\n"
		
		if request.user.is_authenticated:
			user=request.user
			create_order=Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()

			order_id=create_order.pk
			for product in cart_products():
				product_id=product.id
				if product.on_sale:
					price=product.sale_price
				else:
					price=product.price
				for key,value in quantities().items():
					if int(key)==product.id:
						create_order_item=OrderItem(order_id=order_id,product_id=product_id,user=user,quantity=value,price=price)
						create_order_item.save()
			for key in list(request.session.keys()):
				if key=="session_key":
					del request.session[key]

			messages.success(request, "order placed!")
			return redirect('home')
  

		else:
			create_order=Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()
			order_id=create_order.pk
			for product in cart_products():
				product_id=product.id
				if product.on_sale:
					price=product.sale_price
				else:
					price=product.price
				for key,value in quantities().items():
					if int(key)==product.id:
						create_order_item=OrderItem(order_id=order_id,product_id=product_id,quantity=value,price=price)
						create_order_item.save()


			for key in list(request.session.keys()):
				if key=="session_key":
					del request.session[key]

			current_user=Profile.objects.filter(user__id=request.user.id)
			current_user.update(saved_cart="")



			messages.success(request, "order placed!")
			return redirect('home')
	else:
		messages.success(request, "Access denied")
		return redirect('home')
def checkout(request):
	cart=Cart(request)
	cart_products=cart.get_prods
	quantities=cart.get_quants
	totals= cart.cart_total()

	if request.user.is_authenticated:
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		shipping_form=ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, 'payment/checkout.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form})
	else:
		shipping_form=ShippingForm(request.POST or None)
		return render(request, 'payment/checkout.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form})

def billing_info(request):
	if request.POST:
		cart=Cart(request)
		cart_products=cart.get_prods
		quantities=cart.get_quants
		totals= cart.cart_total()

		shipping_info=request.POST
		request.session['shipping_info']=shipping_info

		host=request.get_host
		paypal_dict={
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': totals,
		'item_name': 'Items order',
		'no_shipping': '2',
		'invoice': str(uuid.uuid4()),
		'currency_code': 'KSH',
		'notify_url': 'https://{}{}'.format(host, reverse("paypal-ipn")),
		'return_url': 'https://{}{}'.format(host, reverse("payment_success")),
		'cancel_return': 'https://{}{}'.format(host, reverse("payment_failed")),

		}
		paypal_form=PayPalPaymentsForm(initial=paypal_dict)

		if request.user.is_authenticated:
			billing_form = PaymentForm()
			return render(request, 'payment/billing_info.html', {"paypal_form":paypal_form,'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':request.POST, 'billing_form':billing_form})
		else:
			billing_form = PaymentForm()
			return render(request, 'payment/billing_info.html', {"paypal_form":paypal_form,'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':request.POST})

		shipping_form=request.POST
		return render(request, 'payment/billing_info.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form})

	else:
		messages.success(request, "Access denied")
		return redirect('home')


def payment_success(request):
	return render(request, 'payment/payment_success.html', {})

def payment_failed(request):
	return render(request, 'payment/payment_failed.html', {})

def shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
		orders=Order.objects.filter(shipped=True)
		if request.POST:
			status=request.POST['shipping_status']
			num=request.POST['num']
			order=Order.objects.filter(id=num)
			
			now=datetime.datetime.now()
			order.update(shipped=False)
			
			messages.success(request, "Shipping Status Updated")
			return redirect('home')

		return render(request, 'payment/shipped_dash.html', {'orders':orders})
	else:
		messages.success(request, "Access denied")
		return redirect('home')


def orders(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		order=Order.objects.get(id=pk)
		items=OrderItem.objects.filter(order=pk)
		if request.POST:
			status=request.POST['shipping_status']
			if status =='true':
				order=Order.objects.filter(id=pk)
				now=datetime.datetime.now()
				order.update(shipped=True, date_shipped=now)
			else:
				order=Order.objects.filter(id=pk)
				order.update(shipped=False)
			messages.success(request, "Shipping Status Updated")
			return redirect('home')

		return render(request, 'payment/orders.html', {'order':order,"items":items})

	else:
		messages.success(request, "Access denied")
		return redirect('home')

def Not_shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
		orders=Order.objects.filter(shipped=False)
		if request.POST:
			status=request.POST['shipping_status']
			num=request.POST['num']
			order=Order.objects.filter(id=num)
			
			now=datetime.datetime.now()
			order.update(shipped=True, date_shipped=now)
			
			messages.success(request, "Shipping Status Updated")
			return redirect('home')

		return render(request, 'payment/Not_shipped_dash.html', {'orders':orders})
	else:
		messages.success(request, "Access denied")
		return redirect('home')


