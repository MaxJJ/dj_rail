from .kps_login import doLogin, TOKEN, KPS, Kps
import json
from .cnotes import saveSmgsDraft

client = KPS.client_classifiers
service = client.bind('Classifiers', 'classifiers')


def request(**kwargs):
    req = {}
    if 'Limit' in kwargs.keys():
        req['Limit'] = kwargs['Limit']
    if 'Offset' in kwargs.keys():
        req['Offset'] = kwargs['Offset']
    if 'Filter' in kwargs.keys():
        fltr = kwargs['Filter']
        req['Filter'] = {'Field': fltr[0],
                         'Comparison': fltr[1],
                         'Value': fltr[2].decode('unicode-escape')
                         }
    if 'Sort' in kwargs.keys():
        srt = kwargs['Sort']
        req['Sort'] = {'Field': srt[0],
                       'Order': srt[1]
                       }
    return req


def findStation(qry):
    print('token: '+str(TOKEN))
    if TOKEN['Cookie'] == '':
        doLogin()

    qr = ('%'+qry+'%').encode()
    req_by_name = request(Limit=10, Offset=0, Filter=('Name', 'Like', qr))
    req_by_code = request(Limit=10, Offset=0, Filter=('Code', 'Like', qr))
    with client.settings(raw_response=False):

        result1 = service.getStationList(
            ListRequest=req_by_name,
            _soapheaders={'Accept-Language': 'RU'}
        )
        result2 = service.getStationList(
            ListRequest=req_by_code,
            _soapheaders={'Accept-Language': 'RU'}
        )

        # saveSmgsDraft()

        result = []

        if result1.Count > 0:
            result.extend(result1.Station)
        if result2.Count > 0:
            result.extend(result2.Station)

        res = []

        i = 0
        for st in result:
            i += 1
            st_dict = {}
            for key in st:
                st_dict[key] = st[key]
            res.append(st_dict)
        return res


def findUnits():
    if TOKEN['Cookie'] == '':
        doLogin()
    qr = ('%'+'килогра'+'%').encode()
    req = request(Limit=500, Offset=8, Filter=('Name', 'Like', qr))
    result = service.getMeasurementList(
        MeasurementListRequest=req,
        _soapheaders={'Accept-Language': 'RU'}
    )

    print(result.__dict__)
