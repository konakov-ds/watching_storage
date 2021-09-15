from django.utils import timezone
from datetime import timedelta


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return timezone.now() - visit.entered_at


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)