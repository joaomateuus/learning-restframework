from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id', primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True, blank=True,
        verbose_name='Created at'
    )
    modified_at = models.DateTimeFiel(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        blank=True,
        verbose_name='Modified at'
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name='Active'
    )

    class Meta:
        abstract = True


class Power(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='Name'
    )

    class Meta:
        managed = True
        db_table = 'power'
        verbose_name = 'Power'
        verbose_name_plural = 'Powers'


class Hero(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=128,
        null=False,
        blank=False,
        verbose_name='Name'
    )

    power = models.ForeignKey(
        'Power',
        db_column='id_power',
        on_delete=models.DO_NOTHING,
        null=True,
        db_index=False,
        related_name='powers',
        verbose_name='Power'
    )

    class Meta:
        managed = True
        db_table = 'hero'
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'
