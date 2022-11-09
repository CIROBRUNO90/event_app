import pytest

from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from ..models import *
from .factory import *


@pytest.mark.django_db
class TestServicesBusiness(APITestCase):

    def test_event(self):
        room_test = RoomFakeFactory.make(
            name='room_test',
            capacity=100
        )

        data = {
            'name': 'event_test',
            'event_type': Event.EventType.PUBLIC,
            'room': room_test.id
        }    

        resp = self.client.post(reverse('business_app:event-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Event.objects.filter(
                event_type=Event.EventType.PUBLIC,
                room=room_test).exists()
        )

        # not create an event in the same day
        room_test2 = RoomFakeFactory.make(
            name='room_test',
            capacity=100
        )

        data = {
            'name': 'event_test',
            'event_type': Event.EventType.PUBLIC,
            'room': room_test2.id
        }
        resp = self.client.post(reverse('business_app:event-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)        
        self.assertFalse(
            Event.objects.filter(
                event_type=Event.EventType.PUBLIC,
                room=room_test2).exists()
        )


    def test_room(self):
        data = {
            'name': 'room_test',
            'capacity': 100
        }    

        resp = self.client.post(reverse('business_app:room-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Room.objects.filter(
                name=data['name']).exists())

        # not delete a room associated with an event
        room = Room.objects.all().first()
        event_test = EventFakeFactory.make(
            name='event_test',
            event_type=Event.EventType.PUBLIC,
            room=room
        )

        url = reverse('business_app:room-list') + f'{room.id}/'
        resp = self.client.delete(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_409_CONFLICT)                
        self.assertTrue(
            Room.objects.filter(
                id=room.id).exists())

    def test_booking(self):
        customer = CustomerFakeFactory.make()
        room = RoomFakeFactory.make(
            capacity=10
        )
        event = EventFakeFactory.make(
            event_type=Event.EventType.PUBLIC,
            room=room
        )

        data = {
            'customer': customer.id,
            'event': event.id
        }
        resp = self.client.post(reverse('business_app:booking-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # no booking, no capacity on event
        room.capacity = 1
        room.save()

        customer_2 = CustomerFakeFactory.make()

        data['customer'] = customer_2.id
        resp = self.client.post(reverse('business_app:booking-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(
            Booking.objects.filter(
                customer=customer_2
            ).exists()
        )

        # no booking, event private
        event.event_type = Event.EventType.PRIVATE
        event.save()

        room.capacity = 10
        room.save()

        resp = self.client.post(reverse('business_app:booking-list'), data, format='json')     
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(
            Booking.objects.filter(
                customer=customer_2
            ).exists()
        )
