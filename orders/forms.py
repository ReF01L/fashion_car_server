from ajax_select.fields import AutoCompleteSelectMultipleField
from django.forms import ModelForm


class OrderForm(ModelForm):
    order_items = AutoCompleteSelectMultipleField('order_items')
