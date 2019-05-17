from .kps_login import doLogin, TOKEN, KPS, Kps
from enum import Enum


class ApplicationType(Enum):
    PAPER = 'CNOTE_APPLICATION_TYPE_PAPER'
    ELECTRONIC = 'CNOTE_APPLICATION_TYPE_ELECTRONIC'
    FORM = 'CNOTE_APPLICATION_TYPE_FORM'


class SmgsConsignor:
    def __init__(self):

        # Vai nosūtītājs ir fiziskā persona
        self.IsPhysicalPersonConsignor = False
        # Kravas nosūtītāja KLR ID
        self.ConsignorCustomerId = ''
        # Kravas nosūtītāja adrese
        self.ConsignorAddress = ''
        # Kravas nosūtītāja adrese: Iela, nams
        self.ConsignorStreetAddress = ''
        # Kravas nosūtītāja adrese: Pilsēta
        self.ConsignorCity = ''
        # Kravas nosūtītāja adrese: Pasta indekss
        self.ConsignorPostalCode = ''
        # Kravas nosūtītāja tālrunis.
        self.ConsignorPhone = ''
        # Nosūtītāja atzīmes, nesaistošas dzelzceļam. Teksta brīva ievade.
        self.ConsignorNotes = ''

    def consignor(self):
        cnsgnr = {}
        for key in self.__dict__:
            if self.__dict__[key] != '':
                cnsgnr[key] = self.__dict__[key]
        return cnsgnr


class SmgsConsignee:
    def __init__(self):
        self.IsPhysicalPersonConsignee = False
        # Kravas saņēmēja klienta ID
        self.ConsigneeCustomerId = ''
        # Kravas saņēmēja kods. Teksta brīva ievade.
        self.ConsigneeCode = ''
        # Kravas saņēmēja nosaukums. Teksta brīva ievade.
        self.ConsigneeName = ''
        # Kravas saņēmēja tālrunis. Teksta brīva ievade.
        self.ConsigneePhone = ''
        # Kravas saņēmēja adrese - valsts. Tiek aizpildīts automātiski no klientu klasifikatora.
        self.ConsigneeCountryCode = ''
        # Kravas saņēmēja adrese: Iela, nams
        self.ConsigneeStreetAddress = ''
        # Kravas saņēmēja adrese: Pilsēta
        self.ConsigneeCity = ''
        # Kravas saņēmēja adrese: Pasta indekss
        self.ConsigneePostalCode = ''
        # Saņēmēja uzņēmuma reģ.nr, ja fiziska persona - pers.kods. Teksta brīva ievade.
        self.ConsigneeRegNumber = ''

    def consignee(self):
        cnsgnee = {}
        for key in self.__dict__:
            if self.__dict__[key] != '':
                cnsgnee[key] = self.__dict__[key]
        return cnsgnee


class FromToStations:
    def __init__(self):
        # Nosūtīšanas stacijas kods
        self.DepartureStationCode = ''
        # Nosūtīšanas stacijas kods
        self.DeliveryStationCode = ''

    def stations(self):
        sts = {}
        for key in self.__dict__:
            sts[key] = self.__dict__[key]
        return sts


class SmgsDraftMainData:
    def __init__(self):
        # Pavadzīmes iesniegšanas veids - papīra, elektroniski
        self.ApplicationTypeCode = 'CNOTE_APPLICATION_TYPE_PAPER'

        # Vai vērtība nav noteikta
        self.IsCargoValueUnknown = True

    def main_data(self):
        m_data = {}
        for key in self.__dict__:
            m_data[key] = self.__dict__[key]
        return m_data


class SmgsDraft:
    def __init__(self):
        self.main_data = SmgsDraftMainData()
        self.consignor = SmgsConsignor()
        self.consignee = SmgsConsignee()
        self.stations = FromToStations()

    def smgsDraft(self):
        smgs_draft = {}
        smgs_draft.update(self.main_data.main_data())
        smgs_draft.update(self.consignor.consignor())
        smgs_draft.update(self.consignee.consignee())
        smgs_draft.update(self.stations.stations())
        return smgs_draft


client = KPS.client_cnotes
service = client.bind('Cnotes', 'cnotes')


def saveSmgsDraft():

    if TOKEN['Cookie'] == '':
        doLogin()

    draft = SmgsDraft()
    draft.stations.DeliveryStationCode = '700007'
    draft.stations.DepartureStationCode = '090609'
    draft.consignor.ConsignorCustomerId = 51224
    draft.consignee.IsPhysicalPersonConsignee = True
    draft.consignee.ConsigneeName = 'Джанибек Абдуллаев'
    draft.consignee.ConsigneeCity = "Алматы"
    draft.consignee.ConsigneeStreetAddress = "ул. дом 23 "
    draft.consignee.ConsigneeCode = "1000"
    draft.consignee.ConsigneeCountryCode = 'KZ'
    draft.consignee.ConsigneePostalCode = '123456'

    data = draft.smgsDraft()
    print(data)
    res = service.saveSmgsDraft(Smgs=data,
                                _soapheaders={'Accept-Language': 'RU', 'UserId': 14716077, 'CompanyId': 51223})

    print(res.__dict__)
