from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .forms import SignupForm, CustomUserChangeForm
# from .models import CustomUser
# get_user_model は、settings.py で AUTH_USER_MODEL に指定されているモデルを取得する関数になります。
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
  add_form = SignupForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['username', 'email', 'phoneNumber', 'date_joined', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
