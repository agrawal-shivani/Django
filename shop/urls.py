from django.conf.urls import url 
from . import views


urlpatterns = [
    url("index",views.index,name="shopHome"),
    url(r'^about/',views.about,name="about us" ),
    url("contact/",views.contact,name="contact us"),
    url("tracker/",views.tracker,name="tracingStatus"),
    url("search/",views.search,name="serach"),
    url("productView/",views.productView,name="productView"),
    url("checkOut/",views.checkOut,name="checkOut"),

]
