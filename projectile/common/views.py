from django.http import JsonResponse

from common.choices import (
    Status,
)


def app_info(request):
    response = {
        'name': 'Remote Kitchen Backend',
        'info': 'The API for remote kitchen',
        'version': '1.0.0',
    }
    return JsonResponse(response)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class ListAPICustomView(ListAPIView):
    permission_classes = ()

    def get_queryset(self, related_fields=None, only_fields=None):
        if related_fields is None:
            related_fields = []
        if only_fields is None:
            only_fields = []
            return self.get_serializer_class().Meta.model(
            ).get_all(
                Status.ACTIVE,
                '-pk',
                related_fields,
                only_fields
            )


class CreateAPICustomView(CreateAPIView):
    permission_classes = ()
    create_data = {}

    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'created_by_id'):
            self.create_data['created_by_id'] = self.request.user.id

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)


class ListCreateAPICustomView(ListCreateAPIView):

    permission_classes = ()
    create_data = {}

    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'created_by_id'):
            self.create_data['created_by_id'] = self.request.user.id

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)

    def add_extra_fields(self, extra_fields):
        for key in extra_fields:
            self.create_data[key] = extra_fields[key]

    def get_queryset(self, related_fields=None, only_fields=None):
        if related_fields is None:
            related_fields = []
        if only_fields is None:
            only_fields = []
            return self.get_serializer_class().Meta.model(
            ).get_all(
                Status.ACTIVE,
                '-pk',
                related_fields,
                only_fields
            )


class RetrieveUpdateDestroyAPICustomView(RetrieveUpdateDestroyAPIView):

    permission_classes = ()
    create_data = {}
    lookup_field = 'alias'

    def perform_update(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'updated_by_id'):
            self.create_data['updated_by_id'] = self.request.user.id

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)

    def add_extra_fields(self, extra_fields):
        for key in extra_fields:
            self.create_data[key] = extra_fields[key]

    def get_queryset(self):
        return self.get_serializer_class().Meta.model.objects.filter()
