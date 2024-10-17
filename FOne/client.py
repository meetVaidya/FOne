import requests

class FOne:
    def __init__(self, base_url = "https://api.openf1.org/v1"):
        self.base_url = base_url

    def get_drivers(self, driver_number, session_key, output_overflow=False):
        if output_overflow is True:
            url = f"{self.base_url}/drivers"
            params = {
                "driver_number": driver_number,
                "session_key": session_key
            }
            params = {k: v for k, v in params.items() if v is not None}

            print(f"URL with params: {url}?{'&'.join(f'{k}={v}' for k, v in params.items())}")
            response = requests.get(url, params=params)
            drivers = response.json()
            return drivers
        else:
            url = f"{self.base_url}/drivers"
            params = {
                "driver_number": driver_number,
                "session_key": session_key
            }
            params = {k: v for k, v in params.items() if v is not None}
            if params:
                response = requests.get(url, params=params)
                drivers = response.json()
                return drivers
            else:
                raise ValueError("No parameters provided for driver query. Change the value of output_overflow to True for a full list of drivers of all sessions.")

""" Checking if the code is running or not. Will be writing for unittests for testing soon"""
# if __name__ == "__main__":
#     f1 = FOne()
#     drivers = f1.get_drivers(driver_number=1, session_key=9158)
#     print(type(drivers))
