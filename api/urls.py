from django.urls import include, path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'jobs', JobsViewsList)
router.register(r'jobpost', JobsViewsPost, basename='jobpost')

router.register(r'contact', ContactViewsList)
router.register(r'contactpost', ContactViewsPost, basename='contactpost')

router.register(r'dropmail', DropMailViewsList, basename='dropmail')

router.register(r'jobcategory', JobCategoryViewsList, basename='jobcategory')
router.register(r'jobtype', JobTypeViewsList, basename='jobtype')
#router.register(r'sosiallink', SosialLinkViewsList, basename='sosiallink')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
