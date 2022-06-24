from datetime import datetime

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import GoalForm, UserSignUpForm, UserLoginForm
from .models import Goal

class WelcomeView(TemplateView):
    template_name = "goals/index.html"

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goals"
    template_name = "goals/goal_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.goals.all().order_by('-created').values()
        

class DailyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.DAILY).order_by('-created').values()


class WeeklyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.WEEKLY).order_by('-created').values()


class MonthlyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.MONTHLY).order_by('-created').values()


class YearlyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.YEARLY).order_by('-created').values()


class NonExpiredGoalListView(GoalListView):
    model = Goal
    context_object_name = "goals"
    template_name = "goals/goal_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.goals.exclude(expiry__lte=datetime.now()).order_by('-created').values()
        

class NonExpiredDailyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.DAILY).exclude(expiry__lte=datetime.now()).order_by('-created').values()


class NonExpiredWeeklyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.WEEKLY).exclude(expiry__lte=datetime.now()).order_by('-created').values()


class NonExpiredMonthlyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.MONTHLY).exclude(expiry__lte=datetime.now()).order_by('-created').values()


class NonExpiredYearlyGoalListView(GoalListView):
    def get_queryset(self):
        return self.request.user.goals.filter(timespan=Goal.Timespan.YEARLY).exclude(expiry__lte=datetime.now()).order_by('-created').values()


class GoalDetailView(DetailView):
    model = Goal
    context_object_name = "goal"


class GoalDeleteView(DeleteView):
    model = Goal
    success_url = "/goals"
    template_name = "goals/goal_delete.html"


class GoalCreateView(CreateView):
    model = Goal
    success_url = "/goals"
    form_class = GoalForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class GoalUpdateView(UpdateView):
    model = Goal
    success_url = "/goals"
    form_class = GoalForm


class SignupView(CreateView):
    form_class = UserSignUpForm
    template_name = 'goals/register.html'
    success_url = 'goals.list'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('goals.list'))

class LoginInterfaceView(LoginView):
    form_class = UserLoginForm
    template_name = 'goals/login.html'
    success_url = 'goals.list'

class LogoutInterfaceView(LogoutView):
    template_name = 'goals/index.html'
    success_url = 'welcome'

