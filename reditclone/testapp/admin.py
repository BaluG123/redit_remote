from django.contrib import admin
from testapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['id','name','image','video','caption','title','publish','uploaded','edited','status']
    list_filter=('uploaded','status','name')
    search_fields=('caption','title','name')
    prepopulated_fields={'title':('caption',)}
    date_hierarchy='publish'

# Register your models here.
admin.site.register(Post,PostAdmin)
