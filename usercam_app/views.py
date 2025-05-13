import base64
from django.core.files.base import ContentFile
from django.shortcuts import render
from .models import UserDetail

def user_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')
        phone_number = request.POST.get('phone_number')
        photo_data = request.POST.get('photo')

        photo = None
        if photo_data:
            format, imgstr = photo_data.split(';base64,')
            ext = format.split('/')[-1]
            photo = ContentFile(base64.b64decode(imgstr), name=f"{name}_photo.{ext}")

        # Save the actual values to the database
        UserDetail.objects.create(
            name=name,
            age=age,
            dob=dob,
            gender=gender,
            email=email,
            address=address,
            occupation=occupation,
            phone_number=phone_number,
            photo=photo
        )
        return render(request, 'form.html', {'success': True})

    return render(request, 'form.html')
