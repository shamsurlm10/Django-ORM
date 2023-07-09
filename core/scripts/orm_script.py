from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower

def run():
    # print(Restaurant.objects.count())
    # print(Rating.objects.count())
    # print(Sale.objects.count())

    # restaurants = Restaurant.objects.filter(name = 'Pizzeria 1')
    # print(restaurants.count())
    # print(restaurants.get())

    # print(restaurant.exists())
    # pprint(connection.queries)

    # chinese = Restaurant.TypeChoices.CHINESE
    # indian = Restaurant.TypeChoices.INDIAN
    # mexican = Restaurant.TypeChoices.MEXICAN
    # check_type = [chinese, indian, mexican]
    # restaurants = Restaurant.objects.filter(restaurant_type__in=check_type)

    # restaurents=Restaurant.objects.filter(restaurant_type = chinese, name__startswith='C')

    # restaurants = Restaurant.objects.exclude(restaurant_type = 'CH', name__startswith = 'C')

    # restaurants = Restaurant.objects.exclude(restaurant_type__in = check_type)

    # restaurants=Restaurant.objects.filter(name__lt='E')
    # print(restaurants)

    # sales = Sale.objects.filter(income__range=(50,60))
    # print([sale.income for sale in sales])


    # restaurants = Restaurant.objects.order_by("-name")
    # sales = Sale.objects.order_by("datetime")
    # restaurants1 = Restaurant.objects.order_by("name").reverse()
    # print(restaurants)
    # print(restaurants1)
    # print(sales)

    # restaurants = Restaurant.objects.order_by(Lower("name"))
    # print(restaurants)

    chinese = Restaurant.TypeChoices.CHINESE
    sales = Sale.objects.filter(restaurant__restaurant_type= chinese)
    ratings=Rating.objects.filter(restaurant__name__startswith='C')

    print(ratings)
    print("--------")
    print(sales)
    print(connection.queries)
    


