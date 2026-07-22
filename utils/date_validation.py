from datetime import datetime


def valid_date(date):

    formats = [
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%d,%m,%Y",
        "%d.%m.%Y"
    ]

    for fmt in formats:
        try:
            datetime.strptime(date, fmt)
            return True
        except ValueError:
            pass

    return False