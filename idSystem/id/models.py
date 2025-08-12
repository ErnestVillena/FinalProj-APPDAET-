from django.db import models

ID_KIND_CHOICES = [
    ('passport', 'Passport'),
    ('license', "Driver's License"),
    ('nationalid', 'National ID'),
]

class IdCredentials(models.Model): 
    slug = models.SlugField(max_length=250)
    idCred_name = models.CharField(max_length=100, unique=True, verbose_name="Name")
    idCred_addr = models.TextField(blank=True, null=True, verbose_name="Address")
    idCred_dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")

    class Meta:
        verbose_name = "ID Credential"
        verbose_name_plural = "ID Credentials"
    
    def __str__(self):
        return self.idCred_name


class IdType(models.Model):  
    slug = models.SlugField(max_length=250)
    idType_category = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="ID Category")
    idType_number = models.CharField(max_length=101, unique=True, verbose_name="ID Number")
    idType_desc = models.TextField(blank=True, null=True, verbose_name="ID Description")
    idType_issdate = models.DateField(blank=True, null=True, verbose_name="Issue Date")
    idType_expdate = models.DateField(blank=True, null=True, verbose_name="Expiry Date")
    idType_isexp = models.BooleanField(default=False, verbose_name="Expired")
    idType_issauth = models.CharField(max_length=100, blank=True, null=True, verbose_name="Issuing Authority")
    idType_image = models.ImageField(upload_to='images/')
    
    idType_kind = models.CharField(
        max_length=20,
        choices=ID_KIND_CHOICES,
        default='passport',
        verbose_name="ID Kind"
    )

    owner = models.ForeignKey(
        'IdCredentials',
        on_delete=models.CASCADE,
        related_name='id_types',
        verbose_name="Owner",
        default=1
    )

    class Meta:
        verbose_name = "ID Type"
        verbose_name_plural = "ID Types"
        unique_together = ('idType_category', 'idType_number')

    def __str__(self):
        return f"{self.idType_category} ({self.idType_kind})"