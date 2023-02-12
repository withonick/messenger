from django.contrib import admin
from django.urls import path
from messenger import views

urlpatterns = [
    path("", views.index, name="home"),
    path("admin/", admin.site.urls)
]

handler404 = "messenger.views.page_not_found_view"
handler403 = "messenger.views.page_forbidden"
handler400 = "messenger.views.page_bad_request"
# handler500 = "messenger.views.page_internal_server"