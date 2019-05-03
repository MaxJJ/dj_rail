from lxml import etree
from zeep import Plugin, Client, Settings
from requests import Session
from zeep.transports import Transport
from zeep.helpers import serialize_object
import json


TOKEN = {'Cookie': ''}


class KpsLoginPlugin(Plugin):

    def ingress(self, envelope, http_headers, operation):
        print(etree.tostring(envelope, pretty_print=True))
        TOKEN['Cookie'] = http_headers['Set-Cookie']
        return envelope, http_headers

    def egress(self, envelope, http_headers, operation, binding_options):
        print(etree.tostring(envelope, pretty_print=True))
        http_headers.update(
            {'Content-Type': "application/soap+xml"})
        http_headers.update(TOKEN)
        print('headers --- '+str(http_headers))
        return envelope, http_headers


class Kps:

    def __init__(self,):
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        settings = Settings(strict=False, xml_huge_tree=True)

        self.client_login = Client(
            'https://tkps-http.ldz.lv/kpsws-webapp/Login?wsdl',
            settings=settings,
            transport=transport,
            plugins=[KpsLoginPlugin(), ])

        self.client_classifiers = Client(
            'https://tkps-http.ldz.lv:443/kpsws-webapp/Classifiers?wsdl',
            settings=settings,
            transport=transport,
            plugins=[KpsLoginPlugin(), ])


KPS = Kps()


def doLogin():
    # session = Session()
    # session.verify = False

    # transport = Transport(session=session)
    # settings = Settings(strict=False, xml_huge_tree=True)

    # client = Client(
    #     'https://tkps-http.ldz.lv/kpsws-webapp/Login?wsdl', settings=settings,
    #     transport=transport, plugins=[KpsLoginPlugin(), ])

    client = KPS.client_login
    with client.settings(raw_response=False):

        result = client.service.doLogin(
            Username='RLStest', Password='MAXrls123@')

        res = {}
        for key in result:
            res[key] = result[key]
        res['token'] = TOKEN['Cookie']

    return res
