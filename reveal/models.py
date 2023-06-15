from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from datetime import datetime


class Reveal(models.Model):
    enquiring = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='enquiring',
                                  on_delete=models.CASCADE)

    info_attr = models.CharField(max_length=20,
                                 verbose_name='Info asked for')
    created_at = models.DateTimeField(default=datetime.now)

    # generic foreign key allows any content object to be a provider of info
    content_object = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()


def get_content_object(app_label, model, object_id):
    """For use in views"""
    if app_label and model and object_id:
        c_type = get_object_or_404(ContentType, app_label=app_label, model=model)
        return c_type, c_type.get_object_for_this_type(pk=object_id)
    return None, None
