from .models import *
from .views import *
def cycle_processor(request):
    today = today = datetime.now()
    currentCycle = 0
    context = {
        'currentCycle': currentCycle,
        'today':today

    }
    return context
