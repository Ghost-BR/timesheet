# coding: utf-8

import calendar
import random


days_abbr = list(calendar.day_abbr)
days_abbr.insert(0, days_abbr.pop(-1))


def sum_time(time, offset):
    return '{:2s}{:02d}'.format(time[:2], int(time[2:]) + offset)


def generate_time():
    period = []
    for start_time, end_time in (('0800', '1200'), ('1300', '1530')):
        offset = random.randint(0, 15)
        period.append((sum_time(start_time, offset),
                       sum_time(end_time, offset)))
    return period


def generate_week():
    def empty_day():
        return [('', ''), ('', '')]
    week = [generate_time() for _ in range(5)]
    week.insert(0, empty_day())
    week.append(empty_day())
    return week
