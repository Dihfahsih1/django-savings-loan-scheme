from .models import *

def cycle_processor(request):
    currentCycle = Cycle.objects.get(is_active=True)
    return{'currentCycle': currentCycle}
