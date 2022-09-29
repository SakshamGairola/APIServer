# REST And GraphQL API Server

The API can be called from here [GraphQL](https://gqlapiserver.herokuapp.com/gql), it is an interactive web based GraphQL query frontend.

Methods used

## EndPoint for GraphQL

In APIServer.schema.py
`def resolve_branches (self, info, branch):`
method will get the results for the following query
```
query {
  branches(branch:<name of a branch>){
    branch
    bank {
      name
    }
    ifsc
  }
}
```
`id, address, city, district, state` can be a part of the query

## EndPoint for REST

APIServer.views.py contains the following function:
`def apiRestEndpoint(request, branch):` takes `branch` as an argument, contains two request methods for `GET` and `POST` requests returns a `JSONResponse`
