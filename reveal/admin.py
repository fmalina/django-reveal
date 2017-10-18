from reveal.models import Reveal
from django.contrib import admin

class RevealAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reveal, RevealAdmin)
