from google.oauth2 import service_account
import googleapiclient.discovery
from rest_rail.settings import BASE_DIR
import os


class GdrService:

    def __init__(self):
        self.SERVICE_ACCOUNT_FILE =  os.path.join(BASE_DIR, 'myfiles\Rail Files-9cfa8f351039.json')
        self.SCOPES = ['https://www.googleapis.com/auth/drive']



    def _getGdr(self):
        credentials = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        return googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

    def get_gdr_file_list(self):
        return  self._getGdr().files().list().execute()

   