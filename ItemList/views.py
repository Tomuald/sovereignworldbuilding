# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from ItemList.forms import ItemlistModelForm, ItemModelForm

from ItemList.models import Itemlist, Item
from Project.models import Project

##################
###   #VIEWS   ###
##################

@login_required
def itemlist_detail(request, pk):
	itemlist = Itemlist.objects.get(pk=pk)
	
	context = {'itemlist': itemlist}
	
	return render(request, 'SovereignWebsite/itemlist_detail.html', context)

@login_required
def item_detail(request, pk):
	item = Item.objects.get(pk=pk)
	
	context = {'item': item}
	
	return render(request, 'SovereignWebsite/item_detail.html', context)

##################
###   #FORMS   ###
##################

@login_required
def itemlist_create(request, in_project, pk=None):
	in_project = Project.objects.get(id=in_project)
	
	if pk:
		itemlist = Itemlist.objects.get(pk=pk)
	else:
		itemlist = Itemlist()
	
	form = ItemlistModelForm(request.POST or None, initial={'in_project': in_project}, instance=itemlist)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('itemlist-detail', args=[str(itemlist.id)]))
		
	return render(request, 'SovereignWebsite/itemlist_form.html', {'form': form})

@login_required	
def itemlist_delete(request, pk):
	itemlist = get_object_or_404(Itemlist, pk=pk)
	
	if request.method == 'POST':
		itemlist.delete()
		return HttpResponseRedirect(reverse('project-detail', args=[str(itemlist.in_project.id)]))
	
	return render(request, "SovereignWebsite/itemlist_confirm_delete.html", context={'itemlist': itemlist})

@login_required	
def item_create(request, in_itemlist, pk=None):
	in_itemlist = Itemlist.objects.get(id=in_itemlist)
	
	if pk:
		item = get_object_or_404(Item, pk=pk)
	else:
		item = Item()
	
	form = ItemModelForm(in_itemlist, request.POST or None, initial={'in_itemlist': in_itemlist}, instance=item)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('item-detail', args=[str(item.id)]))
	
	return render(request, 'SovereignWebsite/item_form.html', {'form': form})

@login_required	
def item_delete(request, pk):
	item = get_object_or_404(Item, pk=pk)
	
	if request.method == 'POST':
		item.delete()
		return HttpResponseRedirect(reverse('itemlist-detail', args=[str(item.in_itemlist.id)]))
	
	return render(request, "SovereignWebsite/item_confirm_delete.html", context={'item': item})
