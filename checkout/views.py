from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

# Create your views here.
def front_page(request):

	return render(request, 'checkout/front_page.html', {

		})


def checkout(request):

	return render(request, 'checkout/checkout.html', {

		})

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:

        return redirect(str(redirect_to))

    return TemplateResponse(request, 'checkout/checkout.html', {

        'form': form, 
        'payment': payment
        
        })



from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "checkout/checkout.html", context)