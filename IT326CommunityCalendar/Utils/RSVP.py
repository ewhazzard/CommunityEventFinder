class RSVP:
    def __init__(self, RSVP_date, user_id):
        """Class constructor. """
        self._RSVP_date = RSVP_date
        self._user_id = user_id

    # def RSVP(user_id, RSVP_date):

    def get_RSVP_date(self):
        """Getter for the RSVP date variable. """
        return self._RSVP_date

    def get_user_id(self):
        """ Getter for the user id variable. """
        return self._user_id
