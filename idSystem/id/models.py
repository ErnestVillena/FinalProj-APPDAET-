from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IdType (models.Model): #   Model representing an ID type.
    slug = models.SlugField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    idType_category = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="ID Category")
    idType_number = models.CharField(max_length=100, unique=True, verbose_name="ID Number")
    idType_desc = models.TextField(blank=True, null=True, verbose_name="ID Description")
    idType_issdate = models.DateField(blank=True, null=True, verbose_name="Issue Date")
    idType_expdate = models.DateField(blank=True, null=True, verbose_name="Expiry Date")
    idType_issauth = models.CharField(max_length=100, blank=True, null=True, verbose_name="Issuing Authority")
    idType_image = models.ImageField(upload_to='id_image/', default='default.png')

    VERIFIED_CHOICES = [('Pending', 'Pending'), ('Verified', 'Verified'), ('Rejected', 'Rejected')]
    idType_verify_stat = models.CharField(max_length=10, choices=VERIFIED_CHOICES, default='Pending')

    class Meta:
        verbose_name = "ID Type"
        verbose_name_plural = "ID Types"
        unique_together = ('idType_category', 'idType_number')

    def __str__(self):
        return self.idType_category
    
class IdCredentials (models.Model): #   Model representing ID labels.
    slug = models.SlugField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    idCred_name = models.CharField(max_length=100, unique=True, verbose_name="Name")
    idCred_addr = models.TextField(blank=True, null=True, verbose_name="Address")
    idCred_dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")

    class Meta:
        verbose_name = "ID Credential"
        verbose_name_plural = "ID Credentials"
    
    def __str__(self):
        return self.idCred_name

class IdAttachment (models.Model):
    id_type = models.ForeignKey(IdType, on_delete=models.CASCADE, related_name='Attachments')
    image = models.ImageField(upload_to='id_attachments/', default='default.png')

    def __srt__(self):
        return f"Attachment for {self.id_type}"
    
    class Meta:
        verbose_name = "ID Attachment"
        verbose_name_plural = "ID Attachments"