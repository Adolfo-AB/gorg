from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.WelcomeView.as_view(), name="welcome"),

    path("goals", views.NonExpiredGoalListView.as_view(), name="goals.list"),
    path("goals/daily", views.NonExpiredDailyGoalListView.as_view(), name="daily_goals.list"),
    path("goals/weekly", views.NonExpiredWeeklyGoalListView.as_view(), name="weekly_goals.list"),
    path(
        "goals/monthly", views.NonExpiredMonthlyGoalListView.as_view(), name="monthly_goals.list"
    ),
    path("goals/yearly", views.NonExpiredYearlyGoalListView.as_view(), name="yearly_goals.list"),

    path("goals/new", views.GoalCreateView.as_view(), name="goals.new"),
    path("goals/<int:pk>", views.GoalUpdateView.as_view(), name="goals.update"),
    path("goals/<int:pk>/delete", views.GoalDeleteView.as_view(), name="goals.delete"),

    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
