from reveal.models import Reveal
from django.contrib import admin

class RevealAdmin(admin.ModelAdmin):
    list_display = ('enquiring', 'info_attr', 'created_at', 'content_type')
    list_filter = ('info_attr', 'content_type')


admin.site.register(Reveal, RevealAdmin)
