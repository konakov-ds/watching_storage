from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
        }
        for visit in non_closed_visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)