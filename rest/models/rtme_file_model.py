from django.db import models
from gdstorage.storage import GoogleDriveStorage
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "railtransme@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))

class RtmeFileModel(models.Model):
    """Model definition for RtmeFile."""

    content=models.FileField(upload_to='', storage=gd_storage,blank=True,default='')
    file_name=models.CharField(max_length=100,blank=True,default='')
    file_description=models.CharField(max_length=100,blank=True,default='no description')
    gdr_id=models.CharField(max_length=100,default='0000')


    class Meta:
        """Meta definition for RtmeFileModel."""

        verbose_name = 'RtmeFileModel'
        verbose_name_plural = 'RtmeFileModel'

    def __str__(self):
        """Unicode representation of RtmeFileModel."""
        return 

