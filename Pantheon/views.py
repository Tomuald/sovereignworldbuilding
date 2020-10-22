# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from Pantheon.forms import PantheonModelForm, GodModelForm

from Pantheon.models import Pantheon, God
from World.models import Universe, Faction, NPC

##################
###   #VIEWS   ###
##################

@login_required
def pantheon_detail(request, pk):
	pantheon = Pantheon.objects.get(pk=pk)
	
	context = {'pantheon': pantheon}
	
	return render(request, "SovereignWebsite/pantheon_detail.html", context)

@login_required
def god_detail(request, pk):
	god = God.objects.get(pk=pk)
	worshipped_by_npcs = NPC.objects.filter(faiths=god)
	worshipped_by_factions = Faction.objects.filter(faiths=god)
	
	context = {
		'god': god,
		'worshipped_by_npcs': worshipped_by_npcs,
		'worshipped_by_factions': worshipped_by_factions,
	}
	
	return render(request, "SovereignWebsite/god_detail.html", context)
	
	
################
###   #FORMS ###
################

@login_required
def pantheon_create(request, in_universe, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	universe_set = Universe.objects.filter(id=in_universe.id)
	
	if pk:
		pantheon = get_object_or_404(Pantheon, pk=pk)
	else:
		pantheon = Pantheon()
	
	form = PantheonModelForm(universe_set,
							 request.POST or None,
							 initial={'in_universe': in_universe},
							 instance=pantheon
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pantheon-detail', args=[str(pantheon.id)]))
		
	return render(request, 'SovereignWebsite/pantheon_form.html', {'form': form})

@login_required	
def pantheon_delete(request, pk):
	pantheon = get_object_or_404(Pantheon, pk=pk)
	
	if request.method == 'POST':
		pantheon.delete()
		return HttpResponseRedirect(reverse('universe-detail', args=[str(pantheon.in_universe.id)]))
	
	return render(request, "SovereignWebsite/pantheon_confirm_delete.html", context={'pantheon': pantheon})

@login_required	
def god_create(request, in_pantheon, pk=None):
	in_pantheon = Pantheon.objects.get(id=in_pantheon)
	pantheons = Pantheon.objects.filter(in_universe=in_pantheon.in_universe)
	
	if pk:
		god = get_object_or_404(God, pk=pk)
	else:
		god = God()
	
	form = GodModelForm(pantheons,
						request.POST or None,
						initial={'in_pantheon': in_pantheon},
						instance=god
					)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('god-detail', args=[str(god.id)]))
	
	return render(request, 'SovereignWebsite/god_form.html', {'form': form})

@login_required	
def god_delete(request, pk):
	god = get_object_or_404(God, pk=pk)
	
	if request.method == 'POST':
		god.delete()
		return HttpResponseRedirect(reverse('pantheon-detail', args=[str(god.in_pantheon.id)]))
	
	return render(request, "SovereignWebsite/god_confirm_delete.html", context={'god': god})
