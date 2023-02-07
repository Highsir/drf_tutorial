from django.shortcuts import render
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework.viewsets import ReadOnlyModelViewSet

from example.models import FileSys
from example.serializer import ExampleSerializer
import time


class UploadFileViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    datatime = time.time()
    queryset = FileSys.objects.all()
    serializer_class = ExampleSerializer
    renderer_classes = [XLSXRenderer]
    filename = '{}.xlsx'.format(datatime)
