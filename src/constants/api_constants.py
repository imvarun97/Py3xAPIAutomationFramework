# Class - which contains all the endpoints
# Keep the URLs

class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_patch_delete_put(booking_id):
        return f"https://restful-booker.herokuapp.com/booking/{booking_id}"
