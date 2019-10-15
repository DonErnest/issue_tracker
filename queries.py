from datetime import date, timedelta

from django.db.models import Q
from webapp.models import Project, Task
from webapp.models import Type



#Задачи, закрытые за последний месяц (задачи со статусом "завершено" , созданные за последние 30 дней)
q_1 = Q(status__name='завершено') | Q(created_at__lte=date.today(), created_at__gte=date.today()-timedelta(days=30))
Task.objects.filter(q_1)

#Типы задач, встречающиеся в указанном проекте
queryset = Type.objects.filter(tasks__project=Project.objects.get(name='Осилить джанго'))


# Проекты, в которых присутствует задача с указанным словом в описании (слово - "всё")
Project.objects.filter(tasks__description__icontains='всё')


