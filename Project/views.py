# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from Project.forms import ProjectModelForm

from accounts.models import CustomUser
from Project.models import Project
from Campaign.models import Campaign
from World.models import Universe
from ItemList.models import Itemlist

from Project.decorators import project_in_user_library


##################
###   #VIEWS   ###
##################

@login_required
def project_list(request):
	user = CustomUser.objects.get(username=request.user.username)
	projects = user.user_library.all()

	context = {
		'projects': projects,
	}

	return render(request, "project_list.html", context=context)

@login_required
@project_in_user_library
def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)

	campaigns = project.campaign_set.all()
	universes = project.universe_set.all()
	itemlists = project.itemlist_set.all()

	context = {
		'project': project,
		'campaigns': campaigns,
		'universes': universes,
		'itemlists': itemlists,
	}

	return render(request, 'project_detail.html', context=context)

##################
###   #FORMS   ###
##################

@login_required
def project_create(request, pk=None):
	user = CustomUser.objects.get(username=request.user.username)

	if pk:
		project = get_object_or_404(Project, pk=pk)
	else:
		project = Project()

	form = ProjectModelForm(request.POST or None, initial={'created_by': user}, instance=project)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			user.user_library.add(project)
			user.save()
			return HttpResponseRedirect(
					reverse('project-detail',
						args=[
							str(project.id)
					]))

	return render(request, "project_form.html", {'form': form})

@login_required
@project_in_user_library
def project_delete(request, pk):
	project = get_object_or_404(Project, pk=pk)
	user = CustomUser.objects.get(username=request.user.username)

	if request.method == 'POST':
		user.user_library.remove(project)
		user.save()
		project.delete()
		return HttpResponseRedirect(reverse('project-list'))

	return render(request, "project_confirm_delete.html", context={'project': project})
