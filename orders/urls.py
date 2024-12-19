from .views import *
from django.urls import path

urlpatterns=[
    path("place_order/",PlaceOrderView.as_view()),
    path("modify_order/<int:order_id>/",ModifyOrderView.as_view()),
    path("cancel_order/<int:order_id>/",CancelOrderView.as_view()),
    path("customer/<int:customer_id>/total/",CalculateTotalView.as_view())
]