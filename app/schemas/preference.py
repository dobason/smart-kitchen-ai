from pydantic import BaseModel
from typing import Optional

class Preference(BaseModel):
    dietary_restrictions: Optional[str] = None
    cuisine_preferences: Optional[str] = None
    flavor_profiles: Optional[str] = None
    time_constraints: Optional[str] = None
    specific_note: Optional[str] = None