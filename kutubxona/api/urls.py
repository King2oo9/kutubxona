from django.urls import path
from .views import BookView, UserView
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('blogs', BookApiView.as_view()),
#     path('blogs/<int:pk>', DetailApiView.as_view()),
#     path('users', UserApiView.as_view()),
#     path('users/<int:pk>', DetailUser.as_view())
# ]

router = SimpleRouter()

router.register('users', UserView, basename='Users')

router.register('books', BookView, basename='books')

urlpatterns = router.urls
