from django.urls import path
from .views import UserLoginView, user_logout, SignUpView, UpdateProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('my_profile/', UpdateProfileView.as_view(), name="update_profile"),

]