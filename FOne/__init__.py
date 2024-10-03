import requests


class OpenF1API:
    """A Python wrapper for the OpenF1 API."""

    def __init__(self, base_url="https://api.openf1.org/v1/"):
        """Initialize the OpenF1API object."""
        self.base_url = base_url

    def car_data(self, driver_number: int, session_key: str, speed: int = None) -> dict:
        """
        Get car data from the OpenF1 API.

        Args:
            driver_number (int): The driver number.
            session_key (str): The session key.
            speed (int, optional): Filter results for speeds greater than or equal to this value.

        Returns:
            dict: The API response data.
        """

        endpoint = "car_data"
        params = {
            "driver_number": driver_number,
            "session_key": session_key,
        }
        if speed is not None:
            params["speed"] = f">={speed}"  # Add speed filter to parameters

        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)

        # Basic error handling
        response.raise_for_status()
        return response.json()


# Example usage:
api = OpenF1API()

# Get car data for driver 55, session key 9159
car_data = api.car_data(driver_number=55, session_key="9159")
print(car_data)

# Get car data with speed filtering (speed >= 315)
filtered_car_data = api.car_data(driver_number=55, session_key="9159", speed=315)
print(filtered_car_data)
