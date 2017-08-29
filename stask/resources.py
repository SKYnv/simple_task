from django.contrib.auth.models import User
from tastypie.authorization import Authorization, Unauthorized
# from tastypie.http import HttpUnauthorized
from tastypie.resources import fields
from tastypie.resources import ImmediateHttpResponse
from tastypie.resources import ModelResource

from stask import models


class MyTaskResource(ModelResource):
    # poster = fields.ForeignKey(UserResource, 'poster')

    class Meta:
        queryset = models.MyTask.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True
        resource_name ='mytask'
        excludes = ['id']
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        # if bundle.request.user.is_authenticated():
        return super(MyTaskResource, self).obj_create(bundle, **kwargs)
        # raise ImmediateHttpResponse(HttpUnauthorized('Not authenticated'))