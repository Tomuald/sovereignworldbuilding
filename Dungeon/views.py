# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from Dungeon.forms import DungeonModelForm, RoomsetModelForm, RoomModelForm, RoomLootModelForm

from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from World.models import Area
from ItemList.models import Item

from Dungeon.decorators import dungeon_in_user_library, roomset_in_user_library, room_in_user_library, roomloot_in_user_library

##################
###   #VIEWS   ###
##################

@login_required
@dungeon_in_user_library
def dungeon_detail(request, pk):
	dungeon = Dungeon.objects.get(pk=pk)
	
	context = {
		'dungeon': dungeon,
	}
	
	return render(request, 'dungeon_detail.html', context)
	
@login_required
@roomset_in_user_library
def roomset_detail(request, pk):
	roomset = Roomset.objects.get(pk=pk)
	
	context = {'roomset': roomset}
	
	return render(request, 'roomset_detail.html', context)
	
@login_required
@room_in_user_library
def room_detail(request, pk):
	room = Room.objects.get(pk=pk)
	
	context = {
		'room': room,
	}
	
	return render(request, 'room_detail.html', context)

##################
###   #FORMS   ###
##################
	
@login_required
def dungeon_create(request, in_area, pk=None):
	in_area = Area.objects.get(id=in_area)
	areas = Area.objects.filter(in_region=in_area.in_region)
	
	if pk:
		dungeon = get_object_or_404(Dungeon, pk=pk)
	else:
		dungeon = Dungeon()
		
	form = DungeonModelForm(areas,
							request.POST or None,
							initial={'in_area': in_area},
							instance=dungeon
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('dungeon-detail', args=[str(dungeon.id)]))
	
	return render(request, 'dungeon_form.html', {'form': form})

@login_required
@dungeon_in_user_library
def dungeon_delete(request, pk):
	dungeon = get_object_or_404(Dungeon, pk=pk)
	
	if request.method == 'POST':
		dungeon.delete()
		return HttpResponseRedirect(reverse('area-detail', args=[str(dungeon.in_area.id)]))
	
	return render(request, "dungeon_confirm_delete.html", context={'dungeon': dungeon})
	
@login_required
def roomset_create(request, in_dungeon, pk=None):
	in_dungeon = Dungeon.objects.get(id=in_dungeon)
	dungeons = Dungeon.objects.filter(id=in_dungeon.id)
	
	if pk:
		roomset = get_object_or_404(Roomset, pk=pk)
	else:
		roomset = Roomset()
	
	form = RoomsetModelForm(dungeons, request.POST or None, initial={'in_dungeon': in_dungeon}, instance=roomset)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('roomset-detail', args=[str(roomset.id)]))
	
	return render(request, 'roomset_form.html', {'form': form})

@login_required
@roomset_in_user_library
def roomset_delete(request, pk):
	roomset = get_object_or_404(Roomset, pk=pk)
	
	if request.method == 'POST':
		roomset.delete()
		return HttpResponseRedirect(reverse('dungeon-detail', args=[str(roomset.in_dungeon.id)]))
	
	return render(request, "roomset_confirm_delete.html", context={'roomset': roomset})
	
@login_required	
def room_create(request, in_roomset, pk=None):
	in_roomset = Roomset.objects.get(id=in_roomset)
	
	if pk:
		room = get_object_or_404(Room, pk=pk)
	else:
		room = Room()
	
	rooms = Room.objects.filter(in_roomset=in_roomset.id).exclude(id=room.id)
	
	form = RoomModelForm(rooms,
						 request.POST or None,
						 initial={'in_roomset': in_roomset},
						 instance=room
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('room-detail', args=[str(room.id)]))
	
	return render(request, 'room_form.html', {'form': form})

@login_required
@room_in_user_library
def room_delete(request, pk):
	room = get_object_or_404(Room, pk=pk)
	
	if request.method == 'POST':
		room.delete()
		return HttpResponseRedirect(reverse('roomset-detail', args=[str(room.in_roomset.id)]))
	
	return render(request, "room_confirm_delete.html", context={'room': room})
	
@login_required
def roomloot_create(request, in_room):
	in_room = Room.objects.get(id=in_room)
	items = Item.objects.filter(
		in_itemlist__in_project=in_room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project
	)
	
	roomloot = RoomLoot()
	
	form = RoomLootModelForm(request.POST or None, items=items, initial={'in_room': in_room}, instance=roomloot)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('room-detail', args=[str(in_room.id)]))
	
	return render(request, 'roomloot_form.html', {'form': form})

@login_required
@roomloot_in_user_library
def roomloot_delete(request, pk):
	roomloot = RoomLoot.objects.get(pk=pk)
	
	if request.method == 'POST':
		roomloot.delete()
		return HttpResponseRedirect(reverse('room-detail', args=[str(roomloot.in_room.id)]))
	
	return render(request, "roomloot_confirm_delete.html", context={'roomloot': roomloot})
