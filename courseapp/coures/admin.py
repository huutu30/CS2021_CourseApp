from django.contrib import admin


from .models import Category, Course, Tag, Lesson
from django.utils.html import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']

    def img(self, Course):
        if Course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=Course.image.name)
            )

class Media:
    css = {
        'all': ('/static/css/style.css',)
    }
    js = ('/static/js/script.js',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Tag)
