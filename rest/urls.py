from django.urls import path
from .views.place import Places, SearchPlaces, CreatePlace
from .views.order import OrderList, OrdersInWork, OneOrder, NewOrder, InboundDocsView, AddInboundDocView, DeleteOrder
from .views.cargo import NewCargo, DeleteCargo, CargoItemView, CargoByShipmentView, CargoSearchView, FacturasCargo, IndexedCargoView
from .views.shipment import ShipmentView, CreateShipment, ShipmentInfoView, OrdersShipments
from .views.factura import FacturaView, FacturasListView, CreateFactura
from .views.files_view import GdrFilesView
from .views.comments import CommentView, CommentsToOrderListView
from .views.person import PersonView, PersonSearchView, SavePersonView, AllPersonsView
from .views.directories import UnitSearchView, PackageSearchView, CountriesView
from .views.invoice import InvoiceView, CreateShipmentsInvoice, ShipmentsInvoices
from .views.railbill import RailbillView, CreateRailbill, CreateRoadSection
from .views.kps import KpsLogin, KpsFindStation


urlpatterns = [
    path('api/orders', OrderList.as_view()),
    path('api/orders/new', NewOrder.as_view()),
    path('api/orders/inwork', OrdersInWork.as_view()),
    path('api/orders/<int:id>', OneOrder.as_view()),
    path('api/orders/<int:id>/delete', DeleteOrder.as_view()),
    path('api/orders/<int:id>/shipments', OrdersShipments.as_view()),
    path('api/orders/<int:id>/shipments/create', CreateShipment.as_view()),
    path('api/orders/<int:id>/indocs', InboundDocsView.as_view()),
    path('api/orders/<int:id>/indocs/<int:doc_id>', AddInboundDocView.as_view()),


    path('api/places', Places.as_view()),
    path('api/places/search', SearchPlaces.as_view()),
    path('api/places/create', CreatePlace.as_view()),

    path('api/getnewcargo', NewCargo.as_view()),
    path('api/deletecargo/<int:id>', DeleteCargo.as_view()),

    path('api/shipments/<int:id>', ShipmentView.as_view()),
    path('api/shipments/<int:id>/info', ShipmentInfoView.as_view()),
    path('api/shipments/<int:id>/rwb', RailbillView.as_view()),
    path('api/shipments/<int:id>/rwb/create', CreateRailbill.as_view()),
    path('api/shipments/<int:id>/rwb/road_sections/create',
         CreateRoadSection.as_view()),
    path('api/shipments/<int:id>/invoices', ShipmentsInvoices.as_view()),
    path('api/shipments/<int:id>/invoices/create',
         CreateShipmentsInvoice.as_view()),

    path('api/shipments/<int:id>/facturas', FacturasListView.as_view()),
    path('api/shipments/<int:id>/facturas/create', CreateFactura.as_view()),

    path('api/factura/<int:id>', FacturaView.as_view()),
    path('api/factura/<int:id>/cargo', FacturasCargo.as_view()),
    path('api/factura/<int:id>/cargo/<int:cargo_id>', CargoItemView.as_view()),


    path('api/comments/<int:order_id>/comment/<int:id>', CommentView.as_view()),
    path('api/comments/<int:order_id>/order_comments',
         CommentsToOrderListView.as_view()),

    path('api/persons/<int:id>', PersonView.as_view()),
    path('api/persons/save', SavePersonView.as_view()),
    path('api/persons/search', PersonSearchView.as_view()),
    path('api/persons/', AllPersonsView.as_view()),

    path('api/cargo/<int:id>', CargoItemView.as_view()),
    path('api/cargo/of_shipment/<int:id>', CargoByShipmentView.as_view()),
    path('api/cargo/search', CargoSearchView.as_view()),
    path('api/cargo/indexed', IndexedCargoView.as_view()),



    path('api/invoice/<int:id>', InvoiceView.as_view()),


    path('api/directories/units', UnitSearchView.as_view()),
    path('api/directories/packages', PackageSearchView.as_view()),
    path('api/directories/countries', CountriesView.as_view()),

    path('api/kps/login', KpsLogin.as_view()),
    path('api/kps/find_station', KpsFindStation.as_view()),







    path('api/files/gdr', GdrFilesView.as_view()),
]
