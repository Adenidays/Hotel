from django.shortcuts import render, get_object_or_404, redirect

from .form import BookingApplicationForm
from .models import Room, BookingApplication, RoomFeature


def start_page(request):
    return render(request, 'start_page.html')


def room_list(request):
    non_booked_rooms = Room.objects.filter(is_booked=False)

    return render(request, 'room_list.html', {'rooms': non_booked_rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'room_detail.html', {'room': room})


def apply_booking(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    total_cost = None  # Initialize total_cost as None

    if request.method == 'POST':
        form = BookingApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            booking = BookingApplication(
                name=data['name'],
                surname=data['surname'],
                room=room,
                check_in_date=data['check_in_date'],
                check_out_date=data['check_out_date'],
            )
            booking.save()
            booking.additional_services.set(data['additional_services'])

            # Calculate the total cost
            total_cost = booking.calculate_final_price()

            return render(request, 'booking_success.html', {'room': room, 'total_cost': total_cost})
    else:
        form = BookingApplicationForm()

    return render(request, 'booking_form.html', {'room': room, 'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')


def booking_list(request):
    applications = BookingApplication.objects.all()
    return render(request, 'booking_list.html', {'applications': applications})


def reject_booking(request, application_id):
    application = get_object_or_404(BookingApplication, pk=application_id)

    if not application.is_approved:
        application.is_approved = False

        application.delete()

    return redirect('booking_list')


def approve_booking(request, application_id):
    application = get_object_or_404(BookingApplication, pk=application_id)
    application.is_approved = True
    application.is_rejected = False
    application.delete()
    return redirect('booking_list')
