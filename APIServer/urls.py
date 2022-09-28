from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from APIServer.schema import schema

from . import views

urlpatterns = [
    # csrf_exempt will allow posting other API endpoints to gql(graphQL) and Rest Endpoint
    path('api/<str:branch>', csrf_exempt(views.apiRestEndpoint), name='apiRestEndpoint'),
    path("gql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
