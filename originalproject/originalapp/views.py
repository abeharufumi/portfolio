from django.shortcuts import render, redirect
from django.conf import settings


from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse, reverse_lazy
from django.db.models import Q



# Create your views here.
class MySignupView(CreateView): #ユーザーアカウント登録
  template_name = 'signup.html'
  # model = CustomUser
  # fields= '__all__' # 全てのfieldを表示する
  form_class = SignupForm #UserCreationFormを継承したSignupFormでユーザーを作成していく
  success_url = reverse_lazy('user')
  def form_valid(self, form):
    result = super().form_valid(form)
    user = self.object
    login(self.request, user)
    return result
  
class MyLoginView(LoginView): #ログインを実現する
  template_name = 'registration/login.html'
  form_class = LoginForm

class MyLogoutView(LogoutView):
  template_name = 'logout.html'

class MyUserView(LoginRequiredMixin, TemplateView):
  template_name = 'user.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['user'] = self.request.user
    return context

# class MyOtherView(LoginRequiredMixin, TemplateView):
#   template_name = 'other.html'
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['users'] = CustomUser.objects.exclude(username=self.request.user.username)
#     return context

class CustomListView(LoginRequiredMixin, ListView):
  template_name = 'list.html'
  model = CustomUser
  context_object_name = 'results'
  paginate_by = 10
  
  def get_queryset(self, **kwargs):
      queryset = super().get_queryset(**kwargs)
      query = self.request.GET
      if q := query.get('q'): #python3.8以降
          # queryset = queryset.filter(username__icontains=q, email__icontains=q, phoneNumber__icontains=q, statas__icontains=q) #and検索
          queryset = queryset.filter(Q(username__icontains=q)|Q(email__icontains=q)|Q(phoneNumber__icontains=q)|Q(statas__icontains=q)) #or検索

      return queryset.order_by('username')

class CustomDetailView(LoginRequiredMixin, DetailView):
  template_name = 'detail.html'
  model = CustomUser

# class CustomCreateView(LoginRequiredMixin, CreateView):
  # template_name = 'create.html'
  # model = CustomUser
  # fields = '__all__' # 全てのfieldを表示する
  # success_url = reverse_lazy('create') 

class CustomUpdateView(LoginRequiredMixin, UpdateView):
  template_name = 'update.html'
  model = CustomUser
  fields = ('username', 'email', 'phoneNumber', 'statas', 'document', 'memo',)
  success_url = reverse_lazy('user') #ユーザー作成が完了したらどのページへ遷移するか

class CustomDeleteView(LoginRequiredMixin, DeleteView):
  template_name = 'delete.html'
  model = CustomUser
  success_url = reverse_lazy('list')



# -------------------------------------------------------------

    # user_view 関数の引数 request のデータ属性 user は settings.py の AUTH_USER_MODEL に指定したモデルのインスタンスとなります。AUTH_USER_MODEL には models.py で定義した CustomUser を指定しているため、request.user は CustomUser のインスタンス（より具体的にはページにアクセスしてきたユーザーのインスタンス）となりますので、request.user に CustomUser で定義したメソッドを実行させることができます。もちろんメソッドだけでなく、CustomUser に用意されているクラス変数やデータ属性（インスタンス変数）も利用可能です。


# def login_view(request):
#     if request.method == 'POST':
#         next = request.POST.get('next')
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             if user:
#                 login(request, user)
#                 return redirect(to='/login/')
#     else:
#         form = LoginForm()
#     param = {
#         'form': form,
#     }
#     return render(request, 'list.html', param)


    # --------------------------------------------------------------------


# def CustomerCheckBox(request, pk):
  # pass  

# def index(request):
  # documents = CustomUser.objects.all()
  # return render(request, 'index.html', {'documents':documents})

# def basic_upload(request):
  # if request.method == 'POST' and request.FILES['testfile']:
    # myfile = request.FILES['testfile']
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename) #FileSystemStorage.url file内容にアクセスできるurlを返す
    # return render(request, 'basic_upload.html', {'uploaded_file_url':uploaded_file_url})
  # return render(request, 'basic_upload.html')