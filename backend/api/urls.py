# backend/api/urls.py

from django.urls import path
from .views import ForgotPasswordView, ResetPasswordView, VerifyResetCodeView, signin, signup, NCAABBGameListView, MLBGameListView, NFLGameListView, NCAAFBGameListView, NBAGameListView, WNBAGameListView, MLSGameListView

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('verify-reset-code/', VerifyResetCodeView.as_view(), name='verify_reset_code'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('ncaabbgames/', NCAABBGameListView.as_view(), name='ncaabb_game_list'),
    path('mlbgames/', MLBGameListView.as_view(), name='mlb_game_list'),
    path('nflgames/', NFLGameListView.as_view(), name='nfl_game_list'),
    path('ncaafbgames/', NCAAFBGameListView.as_view(), name='ncaafb_game_list'),
    path('nbagames/', NBAGameListView.as_view(), name='nba_game_list'),
    path('wnbagames/', WNBAGameListView.as_view(), name='wnba_game_list'),
    path('mlsgames/', MLSGameListView.as_view(), name='mls_game_list'),
]
