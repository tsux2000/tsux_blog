from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *
from django.shortcuts import resolve_url, redirect
from .const import *

class DataClass:
    def __init__(self):
        self.meta = {
            'description' : '',
            'robots' : '',
            'title' : '',
            'image' : '',
            'site_name' : SITE_NAME,
            'type' : '',
            'locale' : 'ja_JP',
            'favicon' : BASE_DIR + 'static/favicon.ico',
            'color' : USER_COLOR,
            'fb' : { 'app_id' : FB_APP_ID, },
            'twitter' : { 'card_type' : TWITTER_CARD_TYPE, 'site_user' : TWITTER_SITE_USER, },
        }
        self.menu_list = {
            {'name' : '', 'url' : '', 'rank' : '',},
        }
        self.posts = {
            {'thumbnail' : '', 'title' : '', 'description' : '', 'create_date' : '', 'update_date' : '', 'author_img' : '', 'author_name' : '',},
        }
        self.post = {
            'thumbnail' : '',
            'title' : '',
            'description' : '',
            'create_date' : '',
            'update_date' : '',
            'author_img' : '',
            'author_name' : '',
            'contents' : '',
        }
        self.params = {
            'top_page_flg' : '',
            'breadcrumb' :{{ 'title' : 'TOP', 'url' : SITE_URL,},},
            'base_url' : SITE_URL,
            'meta' : self.meta,
            'menu_list' : self.menu_list,
            'main_contents' : '',
            'posts' : self.posts,
            'post' : self.post,
        }

class MainView(TemplateView, DataClass):

    def __init__(self):
        self.param = {
        'key' : 'value',
        }

    def get(self, request):
        return render(request, 'main/index.html', self.params)

    def post(self, request):
        return render(request, 'main/index.html', self.params)

class PostView(TemplateView, DataClass):

    def __init__(self):
        self.params = {
            'key' : 'value',
        }

    def get(self, request, post_slug = 0, user_slug = 0, static_slug = 0):
        return render(request, 'main/post.html', self.params)

class ListView(TemplateView, DataClass):

    def __init__(self):
        self.params = {
            'key' : 'value',
            'search_text': '',
        }

    def get(self, request, search_text = 0, year = 0, month = 0, category_slug = 0, subcategory_slug = 0):
        self.params['search_text'] = search_text
        return render(request, 'main/list.html', self.params)

class SearchView(View):

    def get(self, request):
        get_search_text = request.GET['search_text']
        return redirect('search', search_text = get_search_text)
