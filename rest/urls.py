from django.urls import path
from .views.place import Places,SearchPlaces
from .views.order import OrderList,OrdersInWork,OneOrder,OrderShipments,OrderShipment,NewOrder,InboundDocsView,AddInboundDocView,OrderShipmentCreate
from .views.cargo import NewCargo,DeleteCargo,CargoItemView,CargoByShipmentView,CargoSearchView
from .views.shipment import ShipmentView,CreateShipment,FacturaView,FacturasListView
from .views.files_view import GdrFilesView
from .views.comments import CommentView,CommentsToOrderListView
from .views.person import PersonView,PersonSearchView,SavePersonView
from .views.directories import UnitSearchView,PackageSearchView


from .views.order import ShipmentList
urlpatterns = [
    path('api/orders',OrderList.as_view()),
    path('api/orders/new',NewOrder.as_view()),
    path('api/orders/inwork',OrdersInWork.as_view()),
    path('api/orders/<int:id>',OneOrder.as_view()),
    path('api/orders/<int:id>/shipments',OrderShipments.as_view()),
    path('api/orders/<int:id>/shipments/create',OrderShipmentCreate.as_view()),
    path('api/orders/<int:id>/indocs',InboundDocsView.as_view()),
    path('api/orders/<int:id>/indocs/<int:doc_id>',AddInboundDocView.as_view()),
    

    path('api/places',Places.as_view()),
    path('api/places/search',SearchPlaces.as_view()),
    path('api/getnewcargo',NewCargo.as_view()),
    path('api/deletecargo/<int:id>',DeleteCargo.as_view()),
    
    path('api/shipments/create',CreateShipment.as_view()),
    path('api/shipments',ShipmentList.as_view()),
    path('api/shipments/<int:id>',ShipmentView.as_view()),

    path('api/shipments/<int:id>/facturas/<int:factura_id>',FacturaView.as_view()),
    path('api/shipments/<int:id>/facturas/all',FacturasListView.as_view()),

    path('api/comments/<int:order_id>/comment/<int:id>',CommentView.as_view()),
    path('api/comments/<int:order_id>/order_comments',CommentsToOrderListView.as_view()),

    path('api/persons/<int:id>',PersonView.as_view()),
    path('api/persons/save',SavePersonView.as_view()),
    path('api/persons/search',PersonSearchView.as_view()),

    path('api/cargo/<int:id>',CargoItemView.as_view()),
    path('api/cargo/of_shipment/<int:id>',CargoByShipmentView.as_view()),
    path('api/cargo/search',CargoSearchView.as_view()),


    path('api/directories/units',UnitSearchView.as_view()),
    path('api/directories/packages',PackageSearchView.as_view()),





    path('api/files/gdr',GdrFilesView.as_view()),
]