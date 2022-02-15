from django.shortcuts import render, get_object_or_404, redirect
from customer.models import Customer
from .forms import CustomerForm

def customer_new(request):
    if request.method == 'POST':
        cust_form = CustomerForm(request.POST)
        if cust_form.is_valid():
            clean_data_dict = cust_form.cleaned_data
            print(clean_data_dict)

            customer = Customer.objects.create(
                name=clean_data_dict['name'],
                email=clean_data_dict['email'],
                birthdate = clean_data_dict['birthdate'],
                gender = clean_data_dict['gender'],
            )
            return redirect('customer_detail', pk=customer.pk)
    else:
        cust_form = CustomerForm()
    return render(request, 'customer/customer_edit.html', {'form':cust_form})

# customer detail
def customer_detail(request, pk):
    cust = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer' : cust})

# customer list
def customer_list(request):
    custs = Customer.objects.order_by('name')
    return render(request, 'customer/customer_list.html', {'customers': custs})