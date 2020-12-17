from django import forms
from .models import Customer, Service, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'role', 'account_number', 'address',
                  'city', 'state', 'zipcode', 'email', 'phone_number')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time', 'service_charge')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_image', 'product', 'p_description', 'charge',)
