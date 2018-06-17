from django.urls import path
from . import views

urlpatterns = [
    path('orders',views.OrderList.as_view()),
    path('orders/inwork',views.OrdersInWork.as_view()),
    path('orders/<int:id>',views.OneOrder.as_view()),
    path('orders/<int:id>/shipments',views.OrderShipments.as_view()),
    path('orders/<int:id>/shipments/<int:shipment_id>',views.OrderShipment.as_view()),
    path('shipments',views.ShipmentList.as_view())
]