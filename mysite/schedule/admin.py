from django.contrib import admin
from .models import Meeting


# I registered my Meeting model in the admin panel so I can easily
# add, edit, and delete meetings through Django’s built-in interface.
# This follows what we were shown in lectures when using the admin panel.


admin.site.register(Meeting)