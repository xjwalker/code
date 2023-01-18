# james m amount of meetings by day from 0:00 to 24:00
# no overlaps
# return the amount of hours
from datetime import datetime


def get_sleep_round(m: str):
    # split input into days
    week_days = m.split('\n')
    curr_min_sleep = -1

    for day in week_days:
        day_name, hours = day.split(' ')
        start = hours.split('-')[0]
        end = hours.split('-')[1]

        if day_name != "Mon":  # check for previous day last meeting.
            # yesterday last meeting until first meeting of the current day:
            lmd_time = get_day_obj(0, 0, hours=end)
            agg_minutes = get_day_obj('00', '00', add_day=True) - lmd_time
            diff_minutes = agg_minutes.seconds / 60

            # Current start of day (00:00) until today's first meeting
            some_day = get_day_obj(start.split(':')[0], start.split(':')[1])
            aux_minutes = some_day - get_day_obj('00', '00')
            diff_minutes_until_first_meeting = aux_minutes.seconds / 60
            diff_minutes += diff_minutes_until_first_meeting

            if curr_min_sleep < diff_minutes:
                curr_min_sleep = diff_minutes
        # Last meeting of the day until end of day
        last_meeting_of_current_day = get_day_obj(end.split(':')[0], end.split(':')[1])
        eod = get_day_obj('00', '00', add_day=True)
        last_day_sleep = eod - last_meeting_of_current_day
        last_day_sleep = last_day_sleep.seconds / 60

        if curr_min_sleep < last_day_sleep:
            curr_min_sleep = last_day_sleep

        print(f"{day} had {curr_min_sleep} minutes of sleep")
    return curr_min_sleep


def get_day_obj(hour, minute, hours=None, add_day=False, remove_day=False):
    fmt = '%Y-%m-%d %H:%M:%S'
    day = '2023-01-02'

    if add_day:
        day = '2023-01-03'
    if remove_day:
        day = '2023-01-01'

    if hours:
        return datetime.strptime(f'{day} {hours}:00', fmt)

    return datetime.strptime(f'{day} {hour}:{minute}:00', fmt)


if __name__ == '__main__':
    input_str = "Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu 01:00-23:00\nFri 01:00-23:00\nSat 01:00-23:00\nSun 01:00-21:00"

    print(get_sleep_round(input_str))
