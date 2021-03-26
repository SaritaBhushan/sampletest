SOLUTION 1:
import heapq
result = []
for user in User.objects.all():
    result.append((user.id*(-1),user.name, user.dob))

result
heapq.heapify(result)
result

OUTPUT:
>>> result
[(-1, 'Vaidehi', datetime.date(2012, 8, 8)), (-2, 'Sarita', datetime.date(1981, 8, 17)), (-3, 'Bhushan', datetime.date(1980, 8, 22))]
>>> heapq.heapify(result)
>>> result
[(-3, 'Bhushan', datetime.date(1980, 8, 22)), (-2, 'Sarita', datetime.date(1981, 8, 17)), (-1, 'Vaidehi', datetime.date(2012, 8, 8))]
----------------------------------------
SOLUTION 2:
>>> result1 = User.objects.all().annotate(id1=F('id')*(-1)).values('id1')
>>> result1
<QuerySet [{'id1': -1}, {'id1': -2}, {'id1': -3}]>
>>> result2 = [tuple(i.values()) for i in result1]
>>> heapq.heapify(list(result2))
>>> result2
[(-1,), (-2,), (-3,)]
>>> heapq.heapify(result2)
>>> result2
[(-3,), (-2,), (-1,)]
--------------------------------------------------