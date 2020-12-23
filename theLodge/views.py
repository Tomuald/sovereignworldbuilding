import datetime

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied

from theLodge.models import SharedItemlist, SharedUniverse
from Project.models import Project
from ItemList.models import Itemlist
from World.models import Universe
from accounts.models import CustomUser

from theLodge.forms import ImportItemlistForm, ExportItemlistForm
from theLodge.forms import ExportUniverseForm, ImportUniverseForm
from theLodge.save_functions import save_itemlist, save_universe

from itertools import chain

# Views
@login_required
def theLodge_list_view(request):
    itemlists = SharedItemlist.objects.all()
    universes = SharedUniverse.objects.all()
    shared_objects = sorted(chain(itemlists, universes), key=lambda obj: obj.shared_at, reverse=True)

    context = {'shared_objects': shared_objects}
    #context = {'itemlists': itemlists, 'universes': universes}

    return render(request, 'theLodge.html', context)

@login_required
def shareditemlist_detail(request, pk):
    itemlist = get_object_or_404(SharedItemlist, pk=pk)

    context = {'itemlist': itemlist}

    return render(request, 'shareditemlist.html', context)


# Form Views
@login_required
def import_itemlist(request, pk):
    user = request.user
    projects = user.user_library.all()
    shared_itemlist = get_object_or_404(SharedItemlist, pk=pk)
    itemlist = shared_itemlist.itemlist
    il_name = itemlist.name

    form = ImportItemlistForm(projects, il_name, request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            proj_id = request.POST.get('to_project')
            to_project = get_object_or_404(Project, id=proj_id)

            save_itemlist(itemlist, to_project)

            return HttpResponseRedirect(reverse('project-list'))

    return render(request, 'importitemlist.html', {'form': form})

@login_required
def export_itemlist(request, user_id, pk):
    itemlist = get_object_or_404(Itemlist, id=pk)
    requesting_user = request.user
    user = get_object_or_404(CustomUser, id=user_id)

    if user != requesting_user:
        raise PermissionDenied

    form = ExportItemlistForm(
            request.POST or None,
            initial={'name': itemlist.name, 'itemlist': itemlist, 'shared_by': user}
        )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('theLodge'))

    return render(request, 'exportitemlist.html', {'form': form})

@login_required
def delete_shared_itemlist(request, pk):
    shared_itemlist = get_object_or_404(SharedItemlist, id=pk)

    if shared_itemlist.shared_by != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        shared_itemlist.delete()
        return HttpResponseRedirect(reverse('theLodge'))

    return render(request, 'shared_itemlist_confirm_delete.html', context={'shared_itemlist': shared_itemlist})

@login_required
def shareduniverse_detail(request, pk):
    universe = get_object_or_404(SharedUniverse, id=pk)

    context = {'universe': universe}

    return render(request, 'shareduniverse.html', context=context)

@login_required
def export_universe(request, user_id, pk):
    universe = get_object_or_404(Universe, id=pk)
    requesting_user = request.user
    user = get_object_or_404(CustomUser, id=user_id)

    if user != requesting_user:
        raise PermissionDenied

    form = ExportUniverseForm(
            request.POST or None,
            initial = {'name': universe.name, 'universe': universe, 'shared_by': user},
        )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('theLodge'))

    return render(request, 'exportuniverse.html', {'form': form})

@login_required
def import_universe(request, pk):
    user = request.user
    projects = user.user_library.all()
    shared_universe = get_object_or_404(SharedUniverse, id=pk)
    universe = shared_universe.universe
    universe_name = universe.name

    form = ImportUniverseForm(projects, universe_name, request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            proj_id = request.POST.get('to_project')
            to_project = get_object_or_404(Project, id=proj_id)

            save_universe(universe, to_project)

            return HttpResponseRedirect(reverse('project-list'))

    return render(request, 'importuniverse.html', {'form': form})
