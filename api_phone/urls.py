from django.urls import path
from .views import (
    register_user,
    login_user,
    LogoutView,
)

urlpatterns = [
    path('register', register_user, name='register_user'),
    path('login', login_user, name='login_user'),
    path('logout', LogoutView, name='logout_user'),
    # path('api/spam', mark_number_as_spam, name='mark_number_as_spam'),
    # path('api/search/name', search_by_name, name='search_by_name'),
    # path('api/search/phone', search_by_phone_number, name='search_by_phone_number'),
    # path('api/contact/<int:contact_id>', get_contact_details, name='get_contact_details'),
    # path('api/users', userdetailview.as_view()),
]
