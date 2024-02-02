import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from autoslug import AutoSlugField
from common.choices import Status
from common.custom_model_fields import TimestampImageField

# default method to get file upload path
def get_upload_to(instance, filename):
    return instance.get_upload_to_path(filename)

class BaseModel(models.Model):
    """Common base model will be used to inherit common model fields

    Args:
        models (_type_): _description_
    """
    alias = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        'core.User',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('created by'),
        related_name="%(app_label)s_%(class)s_created_by"
    )

    updated_by = models.ForeignKey(
        'core.User',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('last updated by'),
        related_name="%(app_label)s_%(class)s_updated_by"
    )


    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def get_all(
            self,
            filter_status=None,
            order_by=None,
            related_fields=None,
            only_fields=None
            ):
        if related_fields is None:
            related_fields = []
        if only_fields is None:
            only_fields = []
        if filter_status is None:
            if order_by is None:
                return self.__class__.objects.filter().select_related(*related_fields).only(*only_fields)
            else:
                return self.__class__.objects.filter().select_related(
                    *related_fields
                ).only(
                    *only_fields
                ).order_by(order_by)
        else:
            if order_by is None:
                return self.__class__.objects.filter(
                ).select_related(
                    *related_fields
                ).only(
                    *only_fields
                ).filter(status=filter_status)
            else:
                return self.__class__.objects.filter(
                ).select_related(
                    *related_fields
                ).only(
                    *only_fields
                ).filter(status=filter_status).order_by(order_by)

    def get_all_actives(self):
        """Get all active instances

        Returns:
            QuerySet: A queryset will all active instances for a model
        """
        return self.__class__.objects.filter(status=Status.ACTIVE).order_by('-pk')

    def to_dict(self, _fields=None, _exclude=None):
        from django.forms.models import model_to_dict
        return model_to_dict(self, _fields, _exclude)


class NameSlugDescriptionBaseModel(BaseModel):
    """Base model for name and description base model

    Args:
        BaseModel (django.db.model): A base model that will be used for name, description base model
    """
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='name',
        always_update=True,
        unique=True,
        allow_unicode=True
    )
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class ImageBaseModel(BaseModel):
    image = TimestampImageField(
        upload_to=get_upload_to,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    # method on the class to provide upload path for files specific to these objects
    def get_upload_to_path(self, instance, filename):
        return 'images/'
