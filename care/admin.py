from django.contrib import admin
from care.models import Upload,DonorProfile

# Register your models here.
admin.site.register(DonorProfile)
admin.site.register(Upload)