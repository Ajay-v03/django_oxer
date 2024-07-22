from django.contrib import admin
from  modeltest.models import ModelTest
# Register your models here.

class ModelTestAdmin(admin.ModelAdmin):
    list_display = ('test_name','test_title','test_desc')

admin.site.register(ModelTest,ModelTestAdmin)
