from django.shortcuts import render
from kyaloedua.models import Message, RoomPost
from kyaloedua.models import Department
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room_posts = RoomPost.objects.filter(
        Q(title__icontains=q) |
        Q(topic__icontains=q) |
        Q(body__icontains=q) |
        Q(subtopic__icontains=q)
    )
    departments = Department.objects.all()
    paginator = Paginator(room_posts, 2)
    room_messages = Message.objects.filter(Q(room__topic__icontains=q))

    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)
    room_count = room_posts.count()

    context = {
        'room_posts':  paged_rooms,
        'departments': departments,
        'room_count': room_count,
        'room_messages': room_messages,
    }
    return render(request, 'kyaloedu/home.html', context)







