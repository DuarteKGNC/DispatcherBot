from rest_framework.response import Response
from rest_framework.decorators import  api_view
from .utils import slack_calls, tickets_helper

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

@api_view(['POST'])
def import_ticket(request):
    if 'file' not in request.FILES:
        return Response(status=400, data="No file part in the request")
    file = request.FILES['file']
    if not file.name.endswith('.csv') or '%00' in file.name:
        return Response(status=400, data="Uploaded file is not a CSV")
    try:
        ticket_id, ticket_name, ticket_description, debug_info = tickets_helper.clean_csv(file=file)
        imported_ticket = [ticket_id, ticket_name, ticket_description, debug_info]
    except Exception as e:
        return Response(status=500, data=f"Error processing the file: {str(e)}")
    return Response(status=200, data=imported_ticket)