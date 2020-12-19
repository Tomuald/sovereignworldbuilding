# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from ItemList.forms import ItemlistModelForm, ItemModelForm

from ItemList.models import Itemlist, Item
from Project.models import Project

from ItemList import decorators

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404

##################
###   #VIEWS   ###
##################

@login_required
@decorators.itemlist_in_user_library
def itemlist_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	itemlists = project.itemlist_set.all()
	itemlist = get_object_or_404(itemlists, name=name)

	context = {'itemlist': itemlist}

	return render(request, 'itemlist_detail.html', context)

@login_required
@decorators.item_in_user_library
def item_detail(request, in_project, in_itemlist, name):
	project = Project.objects.get(id=in_project)
	itemlist = project.itemlist_set.get(name=in_itemlist)
	items = project.item_set.filter(in_itemlist=itemlist)
	item = get_object_or_404(items, name=name)

	context = {'item': item}

	return render(request, 'item_detail.html', context)

##################
###   #FORMS   ###
##################

@login_required
@decorators.create_itemlist_in_user_library
def itemlist_create(request, in_project):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()

	itemlist = Itemlist()

	form = ItemlistModelForm(itemlists, request.POST or None, initial={'in_project': in_project}, instance=itemlist)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			itemlist_name = form.cleaned_data['name']
			return HttpResponseRedirect(
					reverse('itemlist-detail',
						args=[
							str(itemlist.in_project.id),
							itemlist_name])
					)

	return render(request, 'itemlist_form.html', {'form': form})

@login_required
@decorators.itemlist_in_user_library
def itemlist_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()
	itemlist = get_object_or_404(itemlists, name=name)

	form = ItemlistModelForm(itemlists, request.POST or None, instance=itemlist)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('itemlist-detail',
						args=[
							str(itemlist.in_project.id),
							str(itemlist.name)
					]))

	return render(request, 'itemlist_form.html', {'form': form})

@login_required
@decorators.itemlist_in_user_library
def itemlist_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()
	itemlist = get_object_or_404(itemlists, name=name)

	if request.method == 'POST':
		itemlist.delete()
		return HttpResponseRedirect(
				reverse('project-detail',
					args=[
						str(itemlist.in_project.id)
				]))

	return render(request, "itemlist_confirm_delete.html", context={'itemlist': itemlist})

@login_required
@decorators.create_item_in_user_library
def item_create(request, in_project, in_itemlist):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()
	in_itemlist = get_object_or_404(itemlists, name=in_itemlist)
	items = in_itemlist.item_set.all()

	item = Item()

	form = ItemModelForm(items, request.POST or None, initial={'in_itemlist': in_itemlist, 'in_project': in_project}, instance=item)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('item-detail',
						args=[
							str(item.in_project.id),
							str(item.in_itemlist.name),
							str(item.name)
					]))

	return render(request, 'item_form.html', {'form': form})

@login_required
@decorators.item_in_user_library
def item_update(request, in_project, in_itemlist, name):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()

	in_itemlist = get_object_or_404(itemlists, name=in_itemlist)
	items = in_itemlist.item_set.all()
	item = get_object_or_404(items, name=name)

	form = ItemModelForm(items, request.POST or None, instance=item)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('item-detail',
							args=[
								str(item.in_project.id), str(item.in_itemlist.name),
								str(item.name)])
					)
	return render(request, 'item_form.html', {'form': form})

@login_required
@decorators.item_in_user_library
def item_delete(request, in_project, in_itemlist, name):
	in_project = Project.objects.get(id=in_project)
	itemlists = in_project.itemlist_set.all()

	in_itemlist = get_object_or_404(itemlists, name=in_itemlist)
	items = in_itemlist.item_set.all()
	item = get_object_or_404(items, name=name)

	if request.method == 'POST':
		item.delete()
		return HttpResponseRedirect(
				reverse('itemlist-detail',
					args=[
						str(item.in_project.id),
						str(item.in_itemlist.name)
				]))

	return render(request, "item_confirm_delete.html", context={'item': item})
