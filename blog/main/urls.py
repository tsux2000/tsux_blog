from django.urls import path
from .views import MainView

urlpatterns = [
    path('', MainView.as_view(), name = 'index'),
    path('search/', MainView.as_view(), name = 'list'),
    path('<post_slug>/', MainView.as_view(), name = 'post'),
    path('archive/<year>/', MainView.as_view(), name = 'list'),
    path('archive/<year>/<month>/', MainView.as_view(), name = 'list'),
    path('category/<category_slug>/', MainView.as_view(), name = 'list'),
    path('category/<category_slug>/subcategory/<subcategory_slug>/', MainView.as_view(), name = 'list'),
    path('author/', MainView.as_view(), name = 'user_list'),
    path('author/<author_slug>/', MainView.as_view(), name = 'index'),
    path('about_blog_q/', MainView.as_view(), name = 'index'),
    path('sitemap/', MainView.as_view(), name = 'index'),
    path('policy/', MainView.as_view(), name = 'index'),
    path('log_in/', MainView.as_view(), name = 'index'),
    path('sign_up/', MainView.as_view(), name = 'index'),
    path('my_page/<user_id>/', MainView.as_view(), name = 'index'),
    path('about_us/', MainView.as_view(), name = 'index'),
]
