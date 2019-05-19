from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Regions(models.Model):
    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    administrative_name = models.CharField(_('Administrative name'), max_length=128, blank=True, null=True)
    comment = models.TextField(_('Comment'), blank=True, null=True)
    munitipal_name = models.CharField(_('Municipal name'), max_length=128, unique=True)
    okato_code = models.CharField(_('OKATO code'), max_length=30, blank=True, null=True, validators=[MinLengthValidator(limit_value=8)])
    oktmo_code = models.CharField(_('OKTMO code'), max_length=30, blank=True, null=True, validators=[MinLengthValidator(limit_value=8)])
    postcode = models.CharField(_('Postcode'), max_length=30, blank=True, null=True)
    state_uuid = models.CharField(_('Unique number in the state address register'), max_length=30, blank=True, null=True, db_index=True)

    def __str__(self):
        return '{} "{}", pk={}'.format(_('Region'), self.munitipal_name, self.pk)
