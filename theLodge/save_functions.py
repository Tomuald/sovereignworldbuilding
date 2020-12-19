def save_itemlist(itemlist, to_project, items):
    itemlist.pk = None
    itemlist.in_project = to_project
    itemlist.save()

    for item in items:
        item.pk = None
        item.in_project = to_project
        item.in_itemlist = itemlist
        item.save()
