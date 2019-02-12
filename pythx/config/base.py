from pythx.models import request as reqmodels


class PythXConfig(dict):
    def __init__(self):
        self["endpoints"] = {
            "production": "https://api.mythx.io/",
            "staging": "https://staging.api.mythx.io/",
        }
        self["timeouts"] = {"access": 600, "refresh": 3600}  # 10m  # 1h
