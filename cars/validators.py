from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validator(year_of_issue: int) -> None:
    year = datetime.today().year
    if year_of_issue > year:
        raise ValidationError(_("The year cannot be greater than the current"))
    elif year_of_issue < year - 100:
        raise ValidationError(_("The year cannot be that old"))
