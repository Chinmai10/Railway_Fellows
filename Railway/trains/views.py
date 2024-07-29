from django.shortcuts import render, redirect,HttpResponseRedirect , HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView,View
from .filters import TrainsFilter
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm,RegisterForm,NumberForm
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model

Users = get_user_model()



# Create your views here.

from .models import Users,Trains,Booking
from django.views.decorators.csrf import csrf_protect



def showHome(request):
    context = {'isHome': True}
    return render(request, 'home.html', context)

class AllTrainsListView(ListView):
    model = Trains
    template_name = 'all.html'
    context_object_name = 'Trains'


class TrainsDetailView(DetailView):
    model = Trains
    template_name = 'train_details.html'
    context_object_name = 'train'



def register_page(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request,'Register.html',context)

@csrf_protect
def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {}
    return render(request,'login.html',context)

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutUserView(View):
    def get(self,request):
        logout(request)
        return redirect('home')


class Bookings(ListView):
    context_object_name='Bookings'
    template_name='all_booked.html'
    def get_queryset(self):
        return Booking.objects.filter(users = self.request.user.username)

def search(request):
    train = Trains()
    types = (('Normal','Normal'),('Express','Express'))

    train = Trains.objects.order_by('-date')
    myFilter = TrainsFilter(request.GET, queryset=train)
    train = myFilter.qs

    context = {
        'Trains': train,
        'myFilter':myFilter,
        'types' : types
    }
    return render(request,'search.html',context)


class profile(DetailView):
    template_name='profile.html'
    model=Users
    slug_field='username'
    slug_url_kwarg='username'
    context_object_name='user'

class BookingCancelDetailView(DetailView):
    context_object_name = 'booking'
    template_name = 'booking_cancel.html'
    def get_queryset(self):
        return Booking.objects.filter(users = self.request.user.username)


def confirm_cancel(request,pk):
    book = Booking.objects.get(id = pk)
    cost = book.num_booked * book.trains.cost
    user_in = book.users
    user_in.balance = user_in.balance+ cost
    user_in.save()
    book.delete()
    return redirect('all_booked')

def confirm_booking(request,pk):
    train =Trains.objects.get(id = pk)
    if not request.user.is_authenticated:
        return redirect('login')
    user = Users.objects.get(username = request.user.username)
    form = NumberForm()

        
    if request.method =='POST':
        form = NumberForm(request.POST)

        if form.is_valid():
            count = int(request.POST['number_book'])
            new_booking = Booking(num_booked=count,users=user,trains=train)
            new_booking.save()
            cost = count * train.cost
            user.balance = user.balance - cost
            user.save()
            train.seats_res = train.seats_res+count
            train.save()
            return redirect('all_booked')
    return render(request,'confirm_booking.html',{'train':train,'form':form})