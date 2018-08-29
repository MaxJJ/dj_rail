from django.urls import path
from .views.place import Places,SearchPlaces
from .views.order import OrderList,OrdersInWork,OneOrder,OrderShipments,OrderShipment,NewOrder
from .views.cargo import NewCargo,DeleteCargo
from .views.shipment import ShipmentView,CreateShipment
from .views.files_view import GdrFilesView
from .views.comments import CommentView,CommentsToOrderListView
from .views.person import PersonView



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
    
    path('api/shipments/create',CreateShipment.as_view()),
    path('api/shipments',ShipmentList.as_view()),
    path('api/shipments/<int:id>',ShipmentView.as_view()),

    path('api/comments/<int:order_id>/comment/<int:id>',CommentView.as_view()),
    path('api/comments/<int:order_id>/order_comments',CommentsToOrderListView.as_view()),

    path('api/persons/<int:id>',PersonView.as_view()),

    path('api/files/gdr',GdrFilesView.as_view()),
]