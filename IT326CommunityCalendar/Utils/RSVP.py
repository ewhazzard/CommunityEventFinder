class RSVP:
    def __init__(self, RSVP_date, user_id):
        self._RSVP_date = RSVP_date
        self._user_id = user_id

    # def RSVP(user_id, RSVP_date):

    def get_RSVP_date(self):
        """returns the rsvp date"""
        return self._RSVP_date

    def get_user_id(self):
        """returns the user id"""
        return self._user_id
