from django.urls import path
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    #path('', ProfileListView.as_view(), name='profile'),
    #path('', BienvenidaView.as_view(), name='bienvenida'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
    path('registrate', SignUpView.as_view(), name='sign_up'),
    #path('sign_in', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]
