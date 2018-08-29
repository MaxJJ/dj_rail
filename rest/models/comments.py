from django.db import models


class Comment(models.Model):
    """Model definition for Comment."""

    comment=models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    order=models.ForeignKey('Order',on_delete=models.CASCADE,default=1,blank=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        

    def __str__(self):
        """Unicode representation of Comment."""
        return "%s : %s" % ("Comment Model id",self.id)
