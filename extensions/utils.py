from . import jalali
from django.utils import timezone
import re


def convert_en_numbers(input_str):
    """
    Converts English numbers to Persian numbers
    :param input_str: String contains English numbers
    :return: New string with Persian numbers
    """
    mapping = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
        '.': '.',
    }
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(input_str))


def jalali_converter(time):
    time = timezone.localtime(time)
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_touple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_touple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = '{} {} {}، ساعت {}:{}'.format(
        convert_en_numbers(time_to_list[2]),
        time_to_list[1],
        convert_en_numbers(time_to_list[0]),
        convert_en_numbers(time.hour),
        convert_en_numbers(time.minute),
    )
    return output
