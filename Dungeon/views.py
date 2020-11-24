# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from Dungeon.forms import DungeonModelForm, RoomsetModelForm, RoomModelForm, RoomLootModelForm

from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from World.models import Area
from ItemList.models import Item
from Project.models import Project

from Dungeon import decorators

##################
###   #VIEWS   ###
##################

@login_required
@decorators.dungeon_in_user_library
def dungeon_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	dungeons = project.dungeon_set.all()
	dungeon = get_object_or_404(dungeons, title=title)

	context = {'dungeon': dungeon}

	return render(request, 'dungeon_detail.html', context)

@login_required
@decorators.roomset_in_user_library
def roomset_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	roomsets = project.roomset_set.all()
	roomset = get_object_or_404(roomsets, name=name)

	context = {'roomset': roomset}

	return render(request, 'roomset_detail.html', context)

@login_required
@decorators.room_in_user_library
def room_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	rooms = project.room_set.all()
	room = get_object_or_404(rooms, name=name)

	context = {'room': room}

	return render(request, 'room_detail.html', context)

##################
###   #FORMS   ###
##################

@login_required
@decorators.create_dungeon_in_user_library
def dungeon_create(request, in_project, in_area):
	in_project = Project.objects.get(id=in_project)
	in_area = in_project.area_set.get(name=in_area)
	dungeons = in_project.dungeon_set.all()

	dungeon = Dungeon()

	form = DungeonModelForm(dungeons,
							request.POST or None,
							initial={'in_project': in_project, 'in_area': in_area},
							instance=dungeon
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('dungeon-detail',
						args=[
							str(dungeon.in_project.id),
							str(dungeon.title)
					]))

	return render(request, 'dungeon_form.html', {'form': form})

@login_required
@decorators.dungeon_in_user_library
def dungeon_update(request, in_project, title):
	in_project = Project.objects.get(id=in_project)
	dungeons = in_project.dungeon_set.all()

	dungeon = get_object_or_404(dungeons, title=title)

	in_area = dungeon.in_area
	form = DungeonModelForm(dungeons,
							request.POST or None,
							initial={'in_project': in_project, 'in_area': in_area},
							instance=dungeon
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('dungeon-detail',
						args=[
							str(dungeon.in_project.id),
							str(dungeon.title)
					]))

	return render(request, 'dungeon_form.html', {'form': form})

@login_required
@decorators.dungeon_in_user_library
def dungeon_delete(request, in_project, title):
	in_project = Project.objects.get(id=in_project)
	dungeons = in_project.dungeon_set.all()

	dungeon = get_object_or_404(dungeons, title=title)

	if request.method == 'POST':
		dungeon.delete()
		return HttpResponseRedirect(
				reverse('area-detail',
					args=[
						str(dungeon.in_project.id),
						str(dungeon.in_area.name)])
				)

	return render(request, "dungeon_confirm_delete.html", context={'dungeon': dungeon})

@login_required
@decorators.create_roomset_in_user_library
def roomset_create(request, in_project, in_dungeon):
	in_project = Project.objects.get(id=in_project)
	in_dungeon = in_project.dungeon_set.get(title=in_dungeon)
	roomsets = in_project.roomset_set.all()

	roomset = Roomset()

	form = RoomsetModelForm(roomsets, request.POST or None, initial={'in_project': in_project, 'in_dungeon': in_dungeon}, instance=roomset)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('roomset-detail',
						args=[
							str(roomset.in_project.id),
							str(roomset.name)
					]))

	return render(request, 'roomset_form.html', {'form': form})

@login_required
@decorators.roomset_in_user_library
def roomset_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	roomsets = in_project.roomset_set.all()

	roomset = get_object_or_404(roomsets, name=name)
	in_dungeon = roomset.in_dungeon

	form = RoomsetModelForm(roomsets, request.POST or None, initial={'in_project': in_project, 'in_dungeon': in_dungeon}, instance=roomset)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('roomset-detail',
						args=[
							str(roomset.in_project.id),
							str(roomset.name)
					]))

	return render(request, 'roomset_form.html', {'form': form})

@login_required
@decorators.roomset_in_user_library
def roomset_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	roomsets = in_project.roomset_set.all()

	roomset = get_object_or_404(roomsets, name=name)

	if request.method == 'POST':
		roomset.delete()
		return HttpResponseRedirect(
				reverse('dungeon-detail',
						args=[
							str(roomset.in_project.id),
							str(roomset.in_dungeon.title)])
				)
	return render(request, "roomset_confirm_delete.html", context={'roomset': roomset})

@login_required
@decorators.create_room_in_user_library
def room_create(request, in_project, in_roomset):
	project = Project.objects.get(id=in_project)
	in_roomset = project.roomset_set.get(name=in_roomset)
	rooms = project.room_set.all()

	room = Room()

	room_exits = in_roomset.room_set.exclude(id=room.id)

	form = RoomModelForm(room_exits,
						 rooms,
						 request.POST or None,
						 initial={'in_project': project, 'in_roomset': in_roomset},
						 instance=room
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('room-detail',
						args=[
							str(room.in_project.id),
							str(room.name)
					]))

	return render(request, 'room_form.html', {'form': form})

@login_required
@decorators.room_in_user_library
def room_update(request, in_project, name):
	project = Project.objects.get(id=in_project)
	rooms = project.room_set.all()

	room = get_object_or_404(rooms, name=name)
	in_roomset = room.in_roomset

	room_exits = in_roomset.room_set.exclude(id=room.id)

	form = RoomModelForm(room_exits,
						 rooms,
						 request.POST or None,
						 instance=room
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('room-detail',
						args=[
							str(room.in_project.id),
							str(room.name)
					]))

	return render(request, 'room_form.html', {'form': form})

@login_required
@decorators.room_in_user_library
def room_delete(request, in_project, name):
	project = Project.objects.get(id=in_project)
	rooms = project.room_set.all()

	room = get_object_or_404(rooms, name=name)

	if request.method == 'POST':
		room.delete()
		return HttpResponseRedirect(
				reverse('roomset-detail',
					args=[
						str(room.in_project.id),
						str(room.in_roomset.name)
				]))
	return render(request, "room_confirm_delete.html", context={'room': room})

@login_required
@decorators.create_roomloot_in_user_library
def roomloot_create(request, in_project, in_room):
	project = Project.objects.get(id=in_project)
	rooms = project.room_set.all()
	in_room = get_object_or_404(rooms, name=in_room)
	items = project.item_set.all()

	roomloot = RoomLoot()

	form = RoomLootModelForm(request.POST or None, items=items, initial={'in_project': in_project, 'in_room': in_room}, instance=roomloot)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('room-detail',
						args=[
							str(roomloot.in_project.id),
							str(roomloot.in_room.name)
					]))

	return render(request, 'roomloot_form.html', {'form': form})

@login_required
@decorators.roomloot_in_user_library
def roomloot_delete(request, in_project, pk):
	project = Project.objects.get(id=in_project)
	roomloots = project.roomloot_set.all()
	roomloot = get_object_or_404(roomloots, pk=pk)

	if request.method == 'POST':
		roomloot.delete()
		return HttpResponseRedirect(
				reverse('room-detail',
					args=[
						str(roomloot.in_project.id),
						str(roomloot.in_room.name)])
				)

	return render(request, "roomloot_confirm_delete.html", context={'roomloot': roomloot})
