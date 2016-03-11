import decimal
import dateutil.parser


def to_decimal(value):
    decimal.getcontext().prec = 2
    try:
        dec_value = decimal.Decimal(value)
    except:
        dec_value = None

    return dec_value


def to_date(value):
    try:
        date_value = dateutil.parser.parse(value)
    except:
        date_value = None

    return date_value
