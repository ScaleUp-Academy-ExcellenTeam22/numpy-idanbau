import numpy as np


def count_days(month: int, year: int) -> int:
    """
    Count days of each year's month
    :param month: Given month to check
    :param year: Given year to check
    :return: number of days that given month in year has
    """
    if month == 12:
        begin_date = f"{year}-{month}-01"
        end_date = f"{year}-{month}-31"

    else:
        if month < 10:
            begin_month = f"-0{month}"
            end_month = f"-0{month + 1}"
        else:
            begin_month = f"-{month}"
            end_month = f"-{month + 1}"

        begin_date = f"{year}{begin_month}-01"
        end_date = f"{year}{end_month}-01"

    return np.datetime64(end_date) - np.datetime64(begin_date)
