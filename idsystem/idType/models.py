from django.db import models

# Create your models here.

class IdType(models.Model):
    """
    Model representing an ID type.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="ID Type Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "ID Type"
        verbose_name_plural = "ID Types"

    def __str__(self):
        return self.name
    
class IdTypeAlias(models.Model):
    """
    Model representing an alias for an ID type.
    """
    title = models.CharField(max_length=100, unique=True, verbose_name="Alias Title")
    id_type = models.ForeignKey(IdType, on_delete=models.CASCADE, related_name='aliases', verbose_name="ID Type")
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "ID Type Alias"
        verbose_name_plural = "ID Type Aliases"
        unique_together = ('title', 'id_type')
    
    def __str__(self):
        return f"{self.title} ({self.id_type.name})"