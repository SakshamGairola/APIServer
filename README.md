# REST And GraphQL API Server

The API can be called from here [GraphQL](https://gqlapiserver.herokuapp.com/gql/), it is an interactive web based GraphQL query frontend.

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

## How to run the application

1. create a virtual environment using `py -m venv <name-of-virtual-environment>` and activating it through `.\<name-of-virtual-environment>\Scripts\activate`
2. Then in the root directory of virtual-environment create a directory `asgmtAPIServer` and run git pull to clone the repository on your local machine
3. To install required dependencies inside `asgmtAPIServer` directory run `pip install -r requirements.txt`
