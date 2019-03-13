from django.urls import path
from .views import MainView, ListView, PostView,SearchView

urlpatterns = [
    path('', MainView.as_view(), name = 'index'),
    path('search/', SearchView.as_view(), name = 'search_from_input'),
    path('search/<search_text>/', ListView.as_view(), name = 'search'),
    path('<post_slug>/', PostView.as_view(), name = 'post'),
    path('archive/<year>/', ListView.as_view(), name = 'archive'),
    path('archive/<year>/<month>/', ListView.as_view(), name = 'archive'),
    path('category/<category_slug>/', ListView.as_view(), name = 'category'),
    path('category/<category_slug>/<subcategory_slug>/', ListView.as_view(), name = 'subcategory'),
    path('author/', ListView.as_view(), name = 'author_list'),
    path('author/<user_slug>/', PostView.as_view(), name = 'author'),
    path('my_page/<user_slug>/', PostView.as_view(), name = 'mypage'),
    path('static/<static_slug>/', PostView.as_view(), name = 'static'),
]
