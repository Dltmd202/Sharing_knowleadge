from django.contrib import admin
from .models import CustomUser, Report_Answer, Report_Question, Report_Class

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Report_Answer)
admin.site.register(Report_Question)
admin.site.register(Report_Class)