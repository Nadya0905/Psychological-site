from django.contrib import admin
from .models import Doctor, User, Grade, Review


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday', 'sex', 'education', 'specialty', 'experience')


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday')
    # search_fields = ('name',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('description', 'grade')
    # search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'grade', 'user', 'doctor', 'pub_date')
    # search_fields = ('name', 'category')
    # list_select_related = ('category',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Review, ReviewAdmin)
