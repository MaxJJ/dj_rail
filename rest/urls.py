from django.urls import path
from .views.place import Places,SearchPlaces
from .views.order import OrderList,OrdersInWork,OneOrder,OrderShipments,OrderShipment,NewOrder
from .views.cargo import NewCargo,DeleteCargo
from .views.shipment import ShipmentView



from .views.order import ShipmentList
urlpatterns = [
    path('api/orders',OrderList.as_view()),
    path('api/orders/new',NewOrder.as_view()),
    path('api/orders/inwork',OrdersInWork.as_view()),
    path('api/orders/<int:id>',OneOrder.as_view()),
    path('api/orders/<int:id>/shipments',OrderShipments.as_view()),
    

    path('api/places',Places.as_view()),
    path('api/places/search',SearchPlaces.as_view()),
    path('api/getnewcargo',NewCargo.as_view()),
    path('api/deletecargo/<int:id>',DeleteCargo.as_view()),
    
    path('api/shipments',ShipmentList.as_view()),
    path('api/shipments/<int:id>',ShipmentView.as_view()),
]