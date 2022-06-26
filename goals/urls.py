from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.WelcomeView.as_view(), name="welcome"),

    path("goals", views.NonExpiredGoalListView.as_view(), name="active.notimespan.goals.list"),
    path("goals/daily", views.NonExpiredDailyGoalListView.as_view(), name="active.daily.goals.list"),
    path("goals/weekly", views.NonExpiredWeeklyGoalListView.as_view(), name="active.weekly.goals.list"),
    path(
        "goals/monthly", views.NonExpiredMonthlyGoalListView.as_view(), name="active.monthly.goals.list"
    ),
    path("goals/yearly", views.NonExpiredYearlyGoalListView.as_view(), name="active.yearly.goals.list"),

    path("goals/all", views.GoalListView.as_view(), name="all.notimespan.goals.list"),
    path("goals/daily/all", views.DailyGoalListView.as_view(), name="all.daily.goals.list"),
    path("goals/weekly/all", views.WeeklyGoalListView.as_view(), name="all.weekly.goals.list"),
    path(
        "goals/monthly/all", views.MonthlyGoalListView.as_view(), name="all.monthly.goals.list"
    ),
    path("goals/yearly/all", views.YearlyGoalListView.as_view(), name="all.yearly.goals.list"),

    path("goals/new", views.GoalCreateView.as_view(), name="goals.new"),
    path("goals/<int:pk>", views.GoalUpdateView.as_view(), name="goals.update"),
    path("goals/<int:pk>/complete", views.GoalCompleteView.as_view(), name="goals.complete"),
    path("goals/<int:pk>/delete", views.GoalDeleteView.as_view(), name="goals.delete"),

    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
