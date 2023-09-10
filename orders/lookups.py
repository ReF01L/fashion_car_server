from ajax_select import register, LookupChannel

from products.models import Product


@register('order_items')
class OrderItemLookup(LookupChannel):
    model = Product

    def get_query(self, q, request):
        return Product.objects.filter(name__icontains=q).order_by('name')[:50]

    def format_item_display(self, item: Product):
        return u"<span class='tag'>%s</span>" % item.name