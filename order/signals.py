from django.db.models.signals import post_save
from django.dispatch import receiver

from cart.models import Cart
from order.models import Order


@receiver(post_save, sender=Order)
def order_created(instance, created, *args, **kwargs):
    if created:
        carts = Cart.objects.filter(user=instance.user, checked=True)
        for cart in carts:
            cart.delete()
