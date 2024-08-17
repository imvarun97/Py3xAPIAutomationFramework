import allure
import pytest
import logging

from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that  create booking status and Booking ID should not be null")
    @allure.description(
        "Creating a booking from payload and verifying that booking id should not be null")
    def test_create_booking_positive(self):
        logger = logging.getLogger(__name__)
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        booking_id = response.json()['bookingid']
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        logger.info(booking_id)

    @pytest.mark.negative
    @allure.title("Verify that Create Booking doesn't work with no payload")
    @allure.description(
        "Creating a Booking with no payload and verify that booking id")
    def test_create_booking_negative(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=500)
