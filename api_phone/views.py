from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


# User Registration
def register_user(request):
    if request.method == "POST":
        phone_number = request.data.get('phone_number')
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        gender = request.data.get('gender')
        dob = request.data.get('dob')
        
        if email is None or name is None or password is None:        
            return Response({'error': 'Required to fill all details'}, status=400)
        else:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'email already exists'}, status=400)
            user = User.objects.create_user(phone_number=phone_number, password=password, name=name, email=email, gender=gender, dob=dob)
            user.save()
            #user = get_object_or_404(User, phone_number=phone_number)
            #return Response(UserSerializer(user).data)
            print("user created")
            return redirect('login_user') 
    return render(request, 'register.html')

# User Login
def login_user(request):
    if request.method == "POST":
        email = request.data.get('email')
        password = request.data.get('password')
        user = get_object_or_404(User, email=email)
        #print(user)
        user = authenticate(User, email=email, password=password)
        #print(user)    
        if user is not None:
            # Generate and return an access token
            login(request, user)
            #return Response({'message': "Login successful"})
            print("login successful")
            return redirect('register_user')
        #return Response({'error': 'Invalid credentials'}, status=400)
    else:
        return render(request, 'login.html')


def LogoutView(request):
    logout(request)
    return redirect('login_user')


# User logout


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])

# # Mark Number as Spam
# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# @csrf_exempt
# def mark_number_as_spam(request):
#     phone_number = request.data.get('phone_number')
#     spam, created = Spam.objects.get_or_create(phone_number=phone_number)
#     spam.spam_likelihood += 1
#     spam.save()
#     return Response({'success': True})

# # Search by Name

# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def search_by_name(request):    
#     name = request.query_params.get('name')
#     results = User.objects.filter(name__istartswith=name) | User.objects.filter(name__icontains=name)
#     serializer = UserSerializer(results, many=True)
#     return Response(serializer.data)

# # Search by Phone Number
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def search_by_phone_number(request):
#     phone_number = request.query_params.get('phone_number')
#     results = User.objects.filter(phone_number=phone_number)
#     serializer = UserSerializer(results, many=True)
#     return Response(serializer.data)

# # Get Contact Details
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def get_contact_details(request, contact_id):
#     contact = get_object_or_404(User, id=contact_id)
#     print(contact)
#     serializer = UserSerializer(contact)
#     return Response(serializer.data)

# # list view for testing purpose
# class userdetailview(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer