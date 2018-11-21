from django.contrib import admin

from libmgmt.models import Book
from libmgmt.models import PublicationHouse
from libmgmt.models import Review
# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','pages','price']
    fields = ['title', 'pages', 'price', 'pub_date', 'publication']
    search_fields = ['title']
    list_filter = ['pages']

    inlines = [ReviewInline]

admin.site.register(Book, BookAdmin)
admin.site.register(PublicationHouse)
