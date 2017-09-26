from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.start), # login/register page
  url(r'^homepage$', views.home), # homepage. all news and weather
  url(r'^settings$', views.settings), # get OR post. user can change his/her settings here
  url(r'^login$', views.login), #post
  url(r'^register$', views.register), #post
  url(r'^news$', views.get_news), # POST request(s) to news API
  url(r'^weather$', views.logout), # POST request(s) to weather API
  url(r'^notes$', views.notes), # user retrieves notes from DB
  url(r'^reading_list/(?P<username>)$', views.reading_list), # publicly available reading list. user can set to private in options
  url(r'^delete_story$', views.delete_story), # POST request for user to delete stories  from reading list
  url(r'^new_note$', views.new_note), # POST new note to database
  url(r'^delete_note$', views.delete_note) # POST that deletes a user's note
]