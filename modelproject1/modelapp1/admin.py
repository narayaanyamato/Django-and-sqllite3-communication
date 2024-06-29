from django.contrib import admin
from modelapp1.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','csr','srollno','cname']
admin.site.register(Student,StudentAdmin)