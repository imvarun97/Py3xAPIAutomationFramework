import allure
import pytest


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that  create booking status and Booking ID should not be null")
    @allure.description(
        "Creating a booking from payload and verifying that booking id should not be null")
    def test_create_booking_positive(self):
        pass
