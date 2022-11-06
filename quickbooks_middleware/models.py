# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


from django.db import models


class Deliveries(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    direction = models.TextField()
    state = models.CharField(max_length=100)
    generation_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'deliveries'


class DocumentKind(models.Model):
    id_kind = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'document_kind'


class DocumentsDelivery(models.Model):
    id_documents_delivery = models.AutoField(primary_key=True)
    delivery = models.ForeignKey(Deliveries, models.DO_NOTHING)
    document_name = models.TextField()
    document_type = models.CharField(max_length=100)
    document_kind = models.ForeignKey(DocumentKind, models.DO_NOTHING, db_column='document_kind')

    class Meta:
        managed = False
        db_table = 'documents_delivery'