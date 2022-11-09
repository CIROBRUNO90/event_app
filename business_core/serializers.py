import datetime

from rest_framework import serializers


from .models import *

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        event = Event.objects.filter(date=datetime.datetime.now().date()).count()
        if event > 0:
            raise serializers.ValidationError("An event is already scheduled for today")
        return data

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        event = data['event']
        if event.event_type == Event.EventType.PRIVATE:
            raise serializers.ValidationError("The event is private, you cannot make a reservation.")
        return data
