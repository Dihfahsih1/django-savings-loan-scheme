from .models import *
from .views import *
def cycle_processor(request):
    today = today = datetime.now()
    if Cycle.objects.get(is_active=True):
        currentCycle = Cycle.objects.get(is_active=True)
    else:
        currentCycle='2020'

    context = {
        'currentCycle': currentCycle,
        'today':today

    }
    return context



