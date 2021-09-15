from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.utils import get_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = [
        {
            'entered_at': localtime(visit.entered_at),
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit)
        }
        for visit in passcard_visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)