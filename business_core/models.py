from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    document_number = models.IntegerField()

    def __str__(self) -> str:
        return f'Customer: {self.id}: {self.first_name} {self.last_name}'

class Room(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return f'Room {self.id} - Capacity: {self.capacity} '

    @property
    def the_room_has_no_event(self):
        event_room = Event.objects.filter(room=self).count()
        return (event_room == 0)

class Event(models.Model):
    class EventType(models.TextChoices):
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'

    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    room = models.ForeignKey('Room', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'Event {self.id}: {self.name} - {self.event_type} - {self.date}'

    @property
    def are_there_any_available_places(self):
        capacity = self.room.capacity
        bookings = Booking.objects.filter(event=self).count()
        return (capacity > bookings)

class Booking(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('customer', 'event',)    

    def __str__(self) -> str:
        return f'Book {self.id}: {self.customer.__str__} - {self.event.__str__}'
