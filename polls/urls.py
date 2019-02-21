from django.urls import path, include
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
   # get the choices for a specific poll and create choices for a specific poll
   path("polls/<int:pk>/choices/", ChoiceList.as_view(), name = 'choice_list'),
   # vote the choice identified by choice_pk under poll <int:pk>
   path("polls/<int:pk>/choices/<int:choice_pk>/vote/",  CreateVote.as_view(), name="create_vote"),
   path("users/", UserCreate.as_view(), name='user_create'),
   path("login/", LoginView.as_view(), name='login')

]

urlpatterns = urlpatterns + router.urls