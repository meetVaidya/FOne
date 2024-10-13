from dataclasses import dataclass

@dataclass
class Driver:
    broadcast_name: str
    country_code: str
    driver_number: int
    first_name: str
    last_name: str
    full_name: str
    headshot_url: str
    meeting_key: str
    name_acronym: str
    session_key: int
    team_colour: str
    team_name: str