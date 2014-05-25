from django.contrib import admin

from django.utils.translation import ugettext as _

from models import *


class NameAdmin(admin.ModelAdmin):
    list_display  = ['name']
admin.site.register(TargetClass,NameAdmin)
admin.site.register(ManyToManyClass,NameAdmin)


class RelationshipAdmin(admin.ModelAdmin):
    list_display  = ['name',"target"]
admin.site.register(OneToOneClass,RelationshipAdmin)
admin.site.register(ForeignKeyClass,RelationshipAdmin)



