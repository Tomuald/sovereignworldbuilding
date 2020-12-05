from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from theLodge.models import SharedItemlist

@login_required
def theLodge_list_view(request):
    itemlists = SharedItemlist.objects.all()

    context = {'itemlists': itemlists}

    return render(request, 'theLodge.html', context)

@login_required
def shareditemlist_detail(request, pk):
    itemlist = get_object_or_404(SharedItemlist, pk=pk)

    context = {'itemlist': itemlist}

    return render(request, 'shareditemlist.html', context)
