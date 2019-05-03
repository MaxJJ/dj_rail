from .kps_login import doLogin, TOKEN, KPS, Kps
import json


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
    print(req)
    return req


def findStation(qry):
    doLogin()
    print(TOKEN)

    client = KPS.client_classifiers
    service = client.bind('Classifiers', 'classifiers')
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
