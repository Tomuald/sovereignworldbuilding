# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from Pantheon.forms import PantheonModelForm, GodModelForm

from Pantheon.models import Pantheon, God
from World.models import Universe, Faction, NPC
from Project.models import Project

from Pantheon import decorators

##################
###   #VIEWS   ###
##################

@login_required
@decorators.pantheon_in_user_library
def pantheon_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	pantheons = project.pantheon_set.all()
	pantheon = get_object_or_404(pantheons, name=name)

	context = {'pantheon': pantheon}

	return render(request, "pantheon_detail.html", context)

@login_required
@decorators.god_in_user_library
def god_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	gods = project.god_set.all()
	god = get_object_or_404(gods, name=name)
	worshipped_by_npcs = project.npc_set.filter(faiths=god)
	worshipped_by_factions = project.faction_set.filter(faiths=god)

	context = {
		'god': god,
		'worshipped_by_npcs': worshipped_by_npcs,
		'worshipped_by_factions': worshipped_by_factions,
	}

	return render(request, "god_detail.html", context)


################
###   #FORMS ###
################

@login_required
@decorators.create_pantheon_in_user_library
def pantheon_create(request, in_project, in_universe):
	in_project = Project.objects.get(id=in_project)
	in_universe = in_project.universe_set.get(name=in_universe)
	pantheons = in_project.pantheon_set.all()

	pantheon = Pantheon()

	form = PantheonModelForm(pantheons,
							 request.POST or None,
							 initial={'in_project': in_project, 'in_universe': in_universe},
							 instance=pantheon
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('pantheon-detail',
						args=[
							str(pantheon.in_project.id),
							str(pantheon.name)
					]))

	return render(request, 'pantheon_form.html', {'form': form})

@login_required
@decorators.pantheon_in_user_library
def pantheon_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	pantheons = in_project.pantheon_set.all()
	pantheon = get_object_or_404(pantheons, name=name)

	in_universe = pantheon.in_universe


	form = PantheonModelForm(pantheons,
							 request.POST or None,
							 initial={'in_project': in_project, 'in_universe': in_universe},
							 instance=pantheon
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('pantheon-detail',
						args=[
							str(pantheon.in_project.id),
							str(pantheon.name)
					]))

	return render(request, 'pantheon_form.html', {'form': form})

@login_required
@decorators.pantheon_in_user_library
def pantheon_delete(request, in_project, name):
	try:
		pantheon = Pantheon.objects.filter(in_project=in_project).get(name=name)
	except ObjectDoesNotExist:
		raise Http404

	if request.method == 'POST':
		pantheon.delete()
		return HttpResponseRedirect(
				reverse('universe-detail',
					args=[
						str(pantheon.in_project.id),
						str(pantheon.in_universe.name)])
				)

	return render(request, "pantheon_confirm_delete.html", context={'pantheon': pantheon})

@login_required
@decorators.create_god_in_user_library
def god_create(request, in_project, in_pantheon):
	in_project = Project.objects.get(id=in_project)
	in_pantheon = in_project.pantheon_set.get(name=in_pantheon)
	gods = in_project.god_set.all()

	god = God()

	form = GodModelForm(gods,
						request.POST or None,
						initial={'in_project': in_project, 'in_pantheon': in_pantheon},
						instance=god
					)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('god-detail',
						args=[
							str(god.in_project.id),
							str(god.name)
					]))

	return render(request, 'god_form.html', {'form': form})

@login_required
@decorators.god_in_user_library
def god_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	gods = in_project.god_set.all()

	god = get_object_or_404(gods, name=name)

	in_pantheon = god.in_pantheon

	form = GodModelForm(gods,
						request.POST or None,
						initial={'in_project': in_project, 'in_pantheon': in_pantheon},
						instance=god
					)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('god-detail',
						args=[
							str(god.in_project.id),
							str(god.name)
					]))

	return render(request, 'god_form.html', {'form': form})

@login_required
@decorators.god_in_user_library
def god_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	gods = in_project.god_set.all()

	god = get_object_or_404(gods, name=name)

	if request.method == 'POST':
		god.delete()
		return HttpResponseRedirect(
				reverse('pantheon-detail',
					args=[
						str(god.in_project.id),
						str(god.in_pantheon.name)])
					)
	return render(request, "god_confirm_delete.html", context={'god': god})
