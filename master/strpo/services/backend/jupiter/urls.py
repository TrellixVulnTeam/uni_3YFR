# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib import admin

from jupiter.utils import collect_urls

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
              ] + collect_urls()
