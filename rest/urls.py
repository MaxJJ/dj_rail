from django.urls import path
from .views.place import Places
from .views.order import OrderList,OrdersInWork,OneOrder,OrderShipments,OrderShipment


from .views.order import ShipmentList
urlpatterns = [
    path('orders',OrderList.as_view()),
    path('orders/inwork',OrdersInWork.as_view()),
    path('orders/<int:id>',OneOrder.as_view()),
    path('orders/<int:id>/shipments',OrderShipments.as_view()),
    path('orders/<int:id>/shipments/<int:shipment_id>',OrderShipment.as_view()),

    path('places',Places.as_view()),
    
    path('shipments',ShipmentList.as_view()),
]