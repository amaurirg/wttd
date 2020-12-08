from django.contrib import admin
from django.utils.html import format_html
from eventex.core.models import Speaker, Contact, Talk


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{0}" />', obj.photo)

    def email(self, obj):
        return obj.contact_set.emails().first()

    def phone(self, obj):
        return obj.contact_set.phones().first()

    website_link.short_description = 'website'
    photo_img.short_description = 'foto'
    email.short_description = 'e-mail'
    phone.short_description = 'telefone'

# class TalkListAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Talk)
admin.site.register(Speaker, SpeakerModelAdmin)
