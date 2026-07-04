from datetime import datetime


def calculate_net_salary(basic, bonus, deduction):

    return basic + bonus - deduction


def attendance_percentage(present, total):

    if total == 0:
        return 0

    return round((present / total) * 100, 2)


def leave_days(start_date, end_date):

    return (end_date - start_date).days + 1


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_time():

    return datetime.now().strftime("%H:%M:%S")
