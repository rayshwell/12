from rest_framework import throttling
class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        "anon":"1000/day"
    }

class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        "User":"1000/day"
    }