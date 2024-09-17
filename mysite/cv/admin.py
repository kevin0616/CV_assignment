from django.contrib import admin

from .models import Personal_info, Education, Work_experience, Skills

admin.site.register(Personal_info)
admin.site.register(Education)
admin.site.register(Work_experience)
admin.site.register(Skills)