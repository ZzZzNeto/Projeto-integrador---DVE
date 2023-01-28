import datetime
from datetime import timedelta
from ..models import Annoucement, Tags

def changeStatus():
    annoucements = Annoucement.objects.all().filter(status='ATIVO')
    

    for annoucement in annoucements:
        if(datetime.date.today() > annoucement.registration_time):
            annoucement.status='finalizado'
            annoucement.save()


def tagStatus():
    tagNew = Tags.objects.filter(tag='Novo')
    annoucements = Annoucement.objects.all().filter(tags__in=tagNew)


    for annoucement in annoucements:
        if(annoucement.creation_time + timedelta(days=3)) >= datetime.date.today():
            annoucement.tags.remove(tagNew[0].id)
            annoucement.save()
        