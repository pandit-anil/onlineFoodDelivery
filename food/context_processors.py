from . models import SystemSetting,Offer
from decimal import Decimal

def System(request):
    sys = SystemSetting.objects.first()
    return {'sys':sys}

def OfferView(request):
    offers = Offer.objects.filter(status = True)[:4]
    for off in offers:
        discounted_price = off.food.price * (Decimal(1) - Decimal(off.discount) / Decimal(100))
        off.discounted_price = round(discounted_price, 2)
    return {'offers':offers}
