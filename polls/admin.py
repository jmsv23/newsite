from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.
class ChoisceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question']}),
		('Informacion de fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoisceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)