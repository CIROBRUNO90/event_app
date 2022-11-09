from django.contrib import admin

from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'document_number')
    list_filter = ('first_name', 'last_name', 'document_number')
    search_fields = ('first_name', 'last_name', )
    readonly_fields = ('id',)
    list_display_links = ('first_name',)    

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')
    list_filter = ('name', )
    search_fields = ('name', )
    readonly_fields = ('id',)
    list_display_links = ('name',)        

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'event_type')
    list_filter = ('name', 'date', 'event_type')
    search_fields = ('name', 'event_type', )
    readonly_fields = ('id',)
    list_display_links = ('name',)            

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'event')
    list_filter = ('customer', 'event')
    search_fields = ('customer', 'event', )
    readonly_fields = ('id',)
    list_display_links = ('customer',)            
