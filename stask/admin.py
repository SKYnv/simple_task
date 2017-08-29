from django.contrib import admin
import stask.models as my_models

# Register your models here.


class MyTaskAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title', 'status', 'time_elapsed', 'is_complete']
    list_display = ['id', 'title', 'status', 'time_elapsed', 'is_complete']
admin.site.register(my_models.MyTask, MyTaskAdmin)