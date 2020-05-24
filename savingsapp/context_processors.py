from .models import *
from .views import *
def cycle_processor(request):
    today = today = datetime.now()
    currentCycle = '2020/2021'
    # if Cycle.objects.get(is_active=True).exist():
    #     currentCycle = Cycle.objects.get(is_active=True)
    # else:
    #     currentCycle='2020/2021'

    context = {
        'currentCycle': currentCycle,
        'today':today

    }
    return context



