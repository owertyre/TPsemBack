from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .schema import schema
from graphene_django.views import GraphQLView
from django.urls import path

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema
    ))),
    path('admin/', admin.site.urls),
]
