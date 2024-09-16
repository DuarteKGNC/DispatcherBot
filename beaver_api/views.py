from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from .utils import slack_calls

@api_view(['GET'])
def get_userid(request):
    users = slack_calls.get_ids()
    return Response(status=200, data=users)


@api_view(['POST'])
def dispatch_tickets(request):
    if not request.data:
        return Response(status=503, data="You need ticket data to make this request")
    data = slack_calls.dispatch(request.data)
    return Response(status=200, data=data)