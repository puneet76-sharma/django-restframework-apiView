from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentCreateSerializer, StudentSerializer
from rest_framework import status

# Authentication and Permission
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


'''

Short Details about Request:-
1) request.data
2) request.method
3) request.POST
4) request.FILES
5) request.GET
6) request.query_params is same as request.GET

'''



'''

Response(data, status=None, template_name=None, headers=None, content_type=None)

'''

######## Function Based APIVIEW ##############

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def StudentAPI(request, pk):

	stu = Student.objects.get(id=pk)

	if request.method=='GET':
		serializer = StudentSerializer(stu)
		return Response(serializer.data, status=status.HTTP_200_OK)

	if request.method=='PUT':
		serializer = StudentCreateSerializer(data=request.data, instance=stu)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method=='PATCH':
		serializer = StudentCreateSerializer(data=request.data, instance=stu, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	if request.method == 'DELETE':
		stu.delete()
		return Response({"msg":"Deleted Successfully!!!"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def Student_API(request):
	if request.method=='GET':
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	if request.method== 'POST':
		data = request.data
		serializer =  StudentCreateSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






#################### Class Based APIView ##########################


from rest_framework.views import APIView

class StudentClass(APIView):

	def post(self, request, format=None):
		data= request.data
		serializer= StudentCreateSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk, format=None):
		data=request.data
		stu = Student.objects.get(id=pk)
		serializer = StudentCreateSerializer(data=data, instance=stu)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def patch(self, request, pk, format=None):
		data=request.data
		stu = Student.objects.get(id=pk)
		serializer = StudentCreateSerializer(data=data, instance=stu, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def get(self,request, pk=None, format=None):
		if pk:
			stu = Student.objects.get(pk=pk)
			serializer = StudentSerializer(stu)

		else:
			stu=Student.objects.all()
			serializer = StudentSerializer(stu, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk, format=None):
		stu = Student.objects.get(pk=pk)
		stu.delete()
		return Response({"msg":"Data Deleted!!!!!"}, status=status.HTTP_200_OK)

import requests
class TicketRequestView(APIView):

	def post(self, request):
		try:

			evtech_chaperonename = request.data['evtech_chaperonename']
			emailaddress = request.data['emailaddress']
			cr676_agency_code = request.data['cr676_agency_code']
			evtech_notes = request.data['evtech_notes']
			cr676_event_name = request.data['cr676_event_name']
			evtech_numberofchildren = request.data['evtech_numberofchildren']
			evtech_actualchildren = request.data['evtech_actualchildren']
			evtech_numberofchaperones = request.data['evtech_numberofchaperones']
			evtech_actualchaperones = request.data['evtech_actualchaperones']
			evtech_eventid= request.data['evtech_eventid@odata.bind']
			evtech_actualtotaltickets = request.data['evtech_actualtotaltickets']
			evtech_totaltickets = request.data['evtech_totaltickets']
			cr676_children_allocate = request.data['cr676_children_allocate']
			cr676_adult_allocate = request.data['cr676_adult_allocate']
			cr676_total_allocated = request.data['cr676_total_allocated']


			url = 'https://kidsupfrontsandbox.crm3.dynamics.com/api/data/v9.1/evtech_ticketrequests'
			headers={
				  	'Connection': 'keep-alive',
					'Accept': 'application/json, text/plain, */*',
					'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCIsImtpZCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCJ9.eyJhdWQiOiJodHRwczovL2tpZHN1cGZyb250c2FuZGJveC5jcm0zLmR5bmFtaWNzLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQxZGNlODE2LTI0Y2QtNGQzNi1hOTNiLWNhNzUyNDc0MTNlMi8iLCJpYXQiOjE2Mjk0NTAwMTcsIm5iZiI6MTYyOTQ1MDAxNywiZXhwIjoxNjI5NDUzOTE3LCJhaW8iOiJFMlpnWUpnME81dnYzN3luR21IWFYyVGQ5MHY1RHdBPSIsImFwcGlkIjoiYjZiMTNjYzAtMDZjNS00NWNlLWI3YzQtMDNhNGMxYzk4MzU1IiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDFkY2U4MTYtMjRjZC00ZDM2LWE5M2ItY2E3NTI0NzQxM2UyLyIsIm9pZCI6ImY0NTU4MTRhLWJkYmUtNDQyNS05Y2M3LWUzNDE5NmMzMGFjOSIsInJoIjoiMC5BU2tBRnVqY1FjMGtOazJwTzhwMUpIUVQ0c0E4c2JiRkJzNUZ0OFFEcE1ISmcxVXBBQUEuIiwic3ViIjoiZjQ1NTgxNGEtYmRiZS00NDI1LTljYzctZTM0MTk2YzMwYWM5IiwidGlkIjoiNDFkY2U4MTYtMjRjZC00ZDM2LWE5M2ItY2E3NTI0NzQxM2UyIiwidXRpIjoiQ2ZvZUF0SkJxMC1TelJjWTZsc2JBQSIsInZlciI6IjEuMCJ9.MvKD04zpqQl96CaN9NIij0TsWTzuN-CHbk8teNFicPmDSj9tNezZSSUZpt8fuk5vxCRKy_aucBnjUNqK37y6uZakjTscx0o8yHDLTRQyOYU261dMpgQKxpEQAJZ1V3p-bMCYbpOh8HW-Xa_SfB5yWHmnTv3kXbL1IkW9gXNJ2uRJQy6z2FC5f7CmviyoHBDWIG1yn043w8RVpbPGu3N0H4slOCf1_mTmnNdzSd5ft6X8PhKbft9gn05lkIV5DklRpYBjF-2SI67WhR_6o_Enviz3ZA-u-6Br1iY3jlt11OzlMNS07PCJsxo-5iOysu8KvV21ndLxbUWo2Q25fRw7gw',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
					'Content-Type': 'application/json',
					'Origin': 'http://experiencehub.kidsupfront.com',
					'Referer': 'http://experiencehub.kidsupfront.com/',
					'Accept-Language': 'en-US,en;q=0.9'
			}


			# data = {
			# 	'evtech_chaperonename': evtech_chaperonename, 
			# 	'emailaddress': emailaddress, 
			# 	'cr676_agency_code': cr676_agency_code, 
			# 	'evtech_notes': evtech_notes, 
			# 	'cr676_event_name': cr676_event_name,
			# 	'evtech_numberofchildren': evtech_numberofchildren,
			# 	'evtech_actualchildren': evtech_actualchildren,
			# 	'evtech_numberofchaperones': evtech_numberofchaperones,
			# 	'evtech_actualchaperones': evtech_actualchaperones,
			# 	'evtech_eventid@odata.bind': evtech_eventid,
			# 	'evtech_actualtotaltickets': evtech_actualtotaltickets,
			# 	'evtech_totaltickets': evtech_totaltickets,
			# 	'cr676_children_allocate': cr676_children_allocate,
			# 	'cr676_adult_allocate': cr676_adult_allocate,
			# 	'cr676_total_allocated': cr676_total_allocated
			# 	}

			data={
				"evtech_chaperonename": "Testing3",
				"emailaddress": "testing3@yopmail.com",
				"cr676_agency_code": "Honda_20-1606302663946",
				"evtech_notes": "Note",
				"cr676_event_name": "Edmonton Event Two",
				"evtech_numberofchildren": 1,
				"evtech_actualchildren": 1,
				"evtech_numberofchaperones": 1,
				"evtech_actualchaperones": 1,
				"evtech_eventid@odata.bind": "evtech_events(8efaf045-86b9-eb11-8236-0022483bc992)",
				"evtech_actualtotaltickets": 2,
				"evtech_totaltickets": 2,
				"cr676_children_allocate": 1,
				"cr676_adult_allocate": 1,
				"cr676_total_allocated": 2
				}

			data="{\"evtech_chaperonename\":\"Testing\",\"emailaddress\":\"testing@yopmail.com\",\"cr676_agency_code\":\"Honda_20-1606302663946\",\"evtech_notes\":\"Note\",\"cr676_event_name\":\"Edmonton Event Two\",\"evtech_numberofchildren\":1,\"evtech_actualchildren\":1,\"evtech_numberofchaperones\":1,\"evtech_actualchaperones\":1,\"evtech_eventid@odata.bind\":\"evtech_events(8efaf045-86b9-eb11-8236-0022483bc992)\",\"evtech_actualtotaltickets\":2,\"evtech_totaltickets\":2,\"cr676_children_allocate\":1,\"cr676_adult_allocate\":1,\"cr676_total_allocated\":2}"

			# r = requests.post(url, headers=headers, data=data)
			import json
			response = requests.post(url, headers=headers, data=data)
			print(response.status_code)
			return Response(response.status_code)
		except Exception as e:
			return Response(e)
			return Response({"error": "please enter valid parameters"})

class TicketRequestNewView(APIView):

	def post(self, request):
		import requests

		url = "http://np.seasiafinishingschool.com:7088/https://kidsupfrontsandbox.crm3.dynamics.com/api/data/v9.1/evtech_ticketrequests"

		payload={
				"evtech_chaperonename": "Testing3",
				"emailaddress": "testing3@yopmail.com",
				"cr676_agency_code": "Honda_20-1606302663946",
				"evtech_notes": "Note",
				"cr676_event_name": "Edmonton Event Two",
				"evtech_numberofchildren": 1,
				"evtech_actualchildren": 1,
				"evtech_numberofchaperones": 1,
				"evtech_actualchaperones": 1,
				"evtech_eventid@odata.bind": "evtech_events(8efaf045-86b9-eb11-8236-0022483bc992)",
				"evtech_actualtotaltickets": 2,
				"evtech_totaltickets": 2,
				"cr676_children_allocate": 1,
				"cr676_adult_allocate": 1,
				"cr676_total_allocated": 2
				}
		headers = {
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCIsImtpZCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCJ9.eyJhdWQiOiJodHRwczovL2tpZHN1cGZyb250c2FuZGJveC5jcm0zLmR5bmFtaWNzLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQxZGNlODE2LTI0Y2QtNGQzNi1hOTNiLWNhNzUyNDc0MTNlMi8iLCJpYXQiOjE2Mjk0NTAwMTcsIm5iZiI6MTYyOTQ1MDAxNywiZXhwIjoxNjI5NDUzOTE3LCJhaW8iOiJFMlpnWUpnME81dnYzN3luR21IWFYyVGQ5MHY1RHdBPSIsImFwcGlkIjoiYjZiMTNjYzAtMDZjNS00NWNlLWI3YzQtMDNhNGMxYzk4MzU1IiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDFkY2U4MTYtMjRjZC00ZDM2LWE5M2ItY2E3NTI0NzQxM2UyLyIsIm9pZCI6ImY0NTU4MTRhLWJkYmUtNDQyNS05Y2M3LWUzNDE5NmMzMGFjOSIsInJoIjoiMC5BU2tBRnVqY1FjMGtOazJwTzhwMUpIUVQ0c0E4c2JiRkJzNUZ0OFFEcE1ISmcxVXBBQUEuIiwic3ViIjoiZjQ1NTgxNGEtYmRiZS00NDI1LTljYzctZTM0MTk2YzMwYWM5IiwidGlkIjoiNDFkY2U4MTYtMjRjZC00ZDM2LWE5M2ItY2E3NTI0NzQxM2UyIiwidXRpIjoiQ2ZvZUF0SkJxMC1TelJjWTZsc2JBQSIsInZlciI6IjEuMCJ9.MvKD04zpqQl96CaN9NIij0TsWTzuN-CHbk8teNFicPmDSj9tNezZSSUZpt8fuk5vxCRKy_aucBnjUNqK37y6uZakjTscx0o8yHDLTRQyOYU261dMpgQKxpEQAJZ1V3p-bMCYbpOh8HW-Xa_SfB5yWHmnTv3kXbL1IkW9gXNJ2uRJQy6z2FC5f7CmviyoHBDWIG1yn043w8RVpbPGu3N0H4slOCf1_mTmnNdzSd5ft6X8PhKbft9gn05lkIV5DklRpYBjF-2SI67WhR_6o_Enviz3ZA-u-6Br1iY3jlt11OzlMNS07PCJsxo-5iOysu8KvV21ndLxbUWo2Q25fRw7gw',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
		'Content-Type': 'application/json',
		'Origin': 'http://experiencehub.kidsupfront.com',
		'Referer': 'http://experiencehub.kidsupfront.com/',
		'Accept-Language': 'en-US,en;q=0.9'
		}

		response = requests.request("POST", url, headers=headers, data=payload)

		print(response.text)
		return Response(response.status_code)
