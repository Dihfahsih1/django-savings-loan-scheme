from .models import *
from .views import *
def cycle_processor(request):
    today = today = datetime.now()
    currentCycle = Cycle.objects.get(is_active=True)
   

    context = {
        'currentCycle': currentCycle,
        'today':today

    }
    return context



