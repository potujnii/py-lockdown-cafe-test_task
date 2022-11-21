import datetime
from app import errors


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get('vaccine'):
            raise errors.NotVaccinatedError("Visitor must have vaccine to enter")
        if datetime.date.today() > visitor.get('vaccine').get('expiration_date'):
            raise errors.OutdatedVaccineError("Your vaccine has expired")
        if not visitor.get('wearing_a_mask'):
            raise errors.NotWearingMaskError('Visitor must wear mask')

        return f'Welcome to {self.name}'
