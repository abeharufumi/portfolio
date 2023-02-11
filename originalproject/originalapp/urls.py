from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CustomListView, CustomDetailView, MySignupView, MySignupView, MyLoginView, MyLogoutView, MyUserView, CustomUpdateView, CustomDeleteView

urlpatterns = [
  path('signup/', MySignupView.as_view(), name='signup'), #ユーザーを作成するためのフォーム
  path('login/', MyLoginView.as_view(), name='login'),
  path('logout/', MyLogoutView.as_view(),name='logout'),
  path('user/', MyUserView.as_view(), name='user'),
  path('update/<int:pk>/', CustomUpdateView.as_view(), name='update'),
  # path('user/<int:pk>/', MyUserView.as_view(), name='user'),
  # path('other/', MyOtherView.as_view(), name='other'),
  # path('create/', CustomCreateView.as_view(), name='create'), #ユーザーを作成するためのフォーム?
  path('list/', CustomListView.as_view(), name='list'), #顧客user作成一覧
  path('detail/<int:pk>/', CustomDetailView.as_view(), name='detail'),
  path('delete/<int:pk>/', CustomDeleteView.as_view(), name='delete'),

  # path('checkbox/<int:pk>/', CustomerCheckBox, name='checkbox'),
  # path('index/', index, name='index'),
  # path('basic/', basic_upload, name='basic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)