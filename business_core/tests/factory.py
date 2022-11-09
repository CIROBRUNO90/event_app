from model_bakery import baker

class CustomerFakeFactory():

    @staticmethod
    def make(**kwargs):
        if not kwargs:
            kwargs={}
        return baker.make('Customer', **kwargs)

class RoomFakeFactory():

    @staticmethod
    def make(**kwargs):
        if not kwargs:
            kwargs={}
        return baker.make('Room', **kwargs)

class EventFakeFactory():

    @staticmethod
    def make(**kwargs):
        if not kwargs:
            kwargs={}
        return baker.make('Event', **kwargs)

class BookingFakeFactory():

    @staticmethod
    def make(**kwargs):
        if not kwargs:
            kwargs={}
        return baker.make('Booking', **kwargs)