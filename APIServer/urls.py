from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from APIServer.schema import schema

from . import views

urlpatterns = [
    path('api', views.apiendpoint, name='apiendpoint'),
    path('api/<int:id>', views.apiendpointid, name='apiendpointid'),
    # csrf_exempt will allow posting other API endpoints to gql(graphQL)
    path("gql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
