from rest_framework.response import Response
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
import requests
import json


@permission_classes((permissions.AllowAny,))
class ZATCAAPI(APIView):
    """ ZATCA API connection over all API phases:
    
        # 1- Reporting API  Phase
        # 2- Clearance API  Phase
        # 3- Compliance CSID API  Phase
        # 4- Compliance Invoice API  Phase
        # 5- Production CSID (Onboarding) API Phase
        # 6- Production CSID (Renewal) API Phase
        
    """
    def get(self, request):
        if request.GET.get('phase'):
            items = self.get_zatca_api(request.GET.get('phase'))

        if items:
            return Response(items.json())
        return Response({
                'Internal Server Error': ' /api/ '
            })

    def post(self, request):
            # Other API
            items = requests.get("https://jsonplaceholder.typicode.com/users")

            return Response(items.json())

    def get_zatca_api(self, type):
        
        auth = "Basic VFVsSlJERkVRME5CTTIxblFYZEpRa0ZuU1ZSaWQwRkJaVE5WUVZsV1ZUTTBTUzhyTlZGQlFrRkJRamRrVkVGTFFtZG5jV2hyYWs5UVVWRkVRV3BDYWsxU1ZYZEZkMWxMUTFwSmJXbGFVSGxNUjFGQ1IxSlpSbUpIT1dwWlYzZDRSWHBCVWtKbmIwcHJhV0ZLYXk5SmMxcEJSVnBHWjA1dVlqTlplRVo2UVZaQ1oyOUthMmxoU21zdlNYTmFRVVZhUm1ka2JHVklVbTVaV0hBd1RWSjNkMGRuV1VSV1VWRkVSWGhPVlZVeGNFWlRWVFZYVkRCc1JGSlRNVlJrVjBwRVVWTXdlRTFDTkZoRVZFbDVUVVJaZUUxcVJUTk9SRUV4VFd4dldFUlVTVEJOUkZsNFRWUkZNMDVFUVRGTmJHOTNVMVJGVEUxQmEwZEJNVlZGUW1oTlExVXdSWGhFYWtGTlFtZE9Wa0pCYjFSQ1YwWnVZVmQ0YkUxU1dYZEdRVmxFVmxGUlRFVjNNVzlaV0d4b1NVaHNhRm95YUhSaU0xWjVUVkpKZDBWQldVUldVVkZFUlhkcmVFMXFZM1ZOUXpSM1RHcEZkMVpxUVZGQ1oyTnhhR3RxVDFCUlNVSkNaMVZ5WjFGUlFVTm5Ua05CUVZSVVFVczViSEpVVm10dk9YSnJjVFphV1dOak9VaEVVbHBRTkdJNVV6UjZRVFJMYlRkWldFb3JjMjVVVm1oTWEzcFZNRWh6YlZOWU9WVnVPR3BFYUZKVVQwaEVTMkZtZERoREwzVjFWVms1TXpSMmRVMU9ielJKUTBwNlEwTkJhVTEzWjFsblIwRXhWV1JGVVZOQ1owUkNLM0JJZDNkbGFrVmlUVUpyUjBFeFZVVkNRWGRUVFZNeGIxbFliR2htUkVsMFRXcE5NR1pFVFhSTlZFVjVUVkk0ZDBoUldVdERXa2x0YVZwUWVVeEhVVUpCVVhkUVRYcEJkMDFFWXpGT1ZHYzBUbnBCZDAxRVFYcE5VVEIzUTNkWlJGWlJVVTFFUVZGNFRWUkJkMDFTUlhkRWQxbEVWbEZSWVVSQmFHRlpXRkpxV1ZOQmVFMXFSVmxOUWxsSFFURlZSVVIzZDFCU2JUbDJXa05DUTJSWVRucGhWelZzWXpOTmVrMUNNRWRCTVZWa1JHZFJWMEpDVTJkdFNWZEVObUpRWm1KaVMydHRWSGRQU2xKWWRrbGlTRGxJYWtGbVFtZE9Wa2hUVFVWSFJFRlhaMEpTTWxsSmVqZENjVU56V2pGak1XNWpLMkZ5UzJOeWJWUlhNVXg2UWs5Q1owNVdTRkk0UlZKNlFrWk5SVTluVVdGQkwyaHFNVzlrU0ZKM1QyazRkbVJJVGpCWk0wcHpURzV3YUdSSFRtaE1iV1IyWkdrMWVsbFRPVVJhV0Vvd1VsYzFlV0l5ZUhOTU1WSlVWMnRXU2xSc1dsQlRWVTVHVEZaT01WbHJUa0pNVkVWMVdUTktjMDFKUjNSQ1oyZHlRbWRGUmtKUlkwSkJVVk5DYjBSRFFtNVVRblZDWjJkeVFtZEZSa0pSWTNkQldWcHBZVWhTTUdORWIzWk1NMUo2WkVkT2VXSkROVFpaV0ZKcVdWTTFibUl6V1hWak1rVjJVVEpXZVdSRlZuVmpiVGx6WWtNNVZWVXhjRVpoVnpVeVlqSnNhbHBXVGtSUlZFVjFXbGhvTUZveVJqWmtRelZ1WWpOWmRXSkhPV3BaVjNobVZrWk9ZVkpWYkU5V2F6bEtVVEJWZEZVelZtbFJNRVYwVFZObmVFdFROV3BqYmxGM1MzZFpTVXQzV1VKQ1VWVklUVUZIUjBneWFEQmtTRUUyVEhrNU1HTXpVbXBqYlhkMVpXMUdNRmt5UlhWYU1qa3lURzVPYUV3eU9XcGpNMEYzUkdkWlJGWlNNRkJCVVVndlFrRlJSRUZuWlVGTlFqQkhRVEZWWkVwUlVWZE5RbEZIUTBOelIwRlJWVVpDZDAxRFFtZG5ja0puUlVaQ1VXTkVRWHBCYmtKbmEzSkNaMFZGUVZsSk0wWlJiMFZIYWtGWlRVRnZSME5EYzBkQlVWVkdRbmROUTAxQmIwZERRM05IUVZGVlJrSjNUVVJOUVc5SFEwTnhSMU5OTkRsQ1FVMURRVEJyUVUxRldVTkpVVU5XZDBSTlkzRTJVRThyVFdOdGMwSllWWG92ZGpGSFpHaEhjRGR5Y1ZOaE1rRjRWRXRUZGpnek9FbEJTV2hCVDBKT1JFSjBPU3N6UkZOc2FXcHZWbVo0ZW5Ka1JHZzFNamhYUXpNM2MyMUZaRzlIVjFaeVUzQkhNUT09OlhsajE1THlNQ2dTQzY2T2JuRU8vcVZQZmhTYnMza0RUalduR2hlWWhmU3M9"
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Accept-Version": "V2",
                       "Accept-Language": "en", "Accept-Encoding": "gzip, deflate, br", "Clearance-Status": "1","OTP":"123345", "Authorization": auth}
        data = {
                "invoiceHash": "+bA1mucVI67H4WCbN/e9J2qUpHTt3TwMdxlkOWTeov8=",
                "uuid": "6f4d20e0-6bfe-4a80-9389-7dabe6620f12",
                "invoice": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPEludm9pY2UgeG1sbnM9InVybjpvYXNpczpuYW1lczpzcGVjaWZpY2F0aW9uOnVibDpzY2hlbWE6eHNkOkludm9pY2UtMiIgeG1sbnM6Y2FjPSJ1cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6c2NoZW1hOnhzZDpDb21tb25BZ2dyZWdhdGVDb21wb25lbnRzLTIiIHhtbG5zOmNiYz0idXJuOm9hc2lzOm5hbWVzOnNwZWNpZmljYXRpb246dWJsOnNjaGVtYTp4c2Q6Q29tbW9uQmFzaWNDb21wb25lbnRzLTIiIHhtbG5zOmV4dD0idXJuOm9hc2lzOm5hbWVzOnNwZWNpZmljYXRpb246dWJsOnNjaGVtYTp4c2Q6Q29tbW9uRXh0ZW5zaW9uQ29tcG9uZW50cy0yIj48ZXh0OlVCTEV4dGVuc2lvbnM+CiAgICA8ZXh0OlVCTEV4dGVuc2lvbj4KICAgICAgICA8ZXh0OkV4dGVuc2lvblVSST51cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6ZHNpZzplbnZlbG9wZWQ6eGFkZXM8L2V4dDpFeHRlbnNpb25VUkk+CiAgICAgICAgPGV4dDpFeHRlbnNpb25Db250ZW50PgogICAgICAgICAgICA8IS0tIFBsZWFzZSBub3RlIHRoYXQgdGhlIHNpZ25hdHVyZSB2YWx1ZXMgYXJlIHNhbXBsZSB2YWx1ZXMgb25seSAtLT4KICAgICAgICAgICAgPHNpZzpVQkxEb2N1bWVudFNpZ25hdHVyZXMgeG1sbnM6c2lnPSJ1cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6c2NoZW1hOnhzZDpDb21tb25TaWduYXR1cmVDb21wb25lbnRzLTIiIHhtbG5zOnNhYz0idXJuOm9hc2lzOm5hbWVzOnNwZWNpZmljYXRpb246dWJsOnNjaGVtYTp4c2Q6U2lnbmF0dXJlQWdncmVnYXRlQ29tcG9uZW50cy0yIiB4bWxuczpzYmM9InVybjpvYXNpczpuYW1lczpzcGVjaWZpY2F0aW9uOnVibDpzY2hlbWE6eHNkOlNpZ25hdHVyZUJhc2ljQ29tcG9uZW50cy0yIj4KICAgICAgICAgICAgICAgIDxzYWM6U2lnbmF0dXJlSW5mb3JtYXRpb24+CiAgICAgICAgICAgICAgICAgICAgPGNiYzpJRD51cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6c2lnbmF0dXJlOjE8L2NiYzpJRD4KICAgICAgICAgICAgICAgICAgICA8c2JjOlJlZmVyZW5jZWRTaWduYXR1cmVJRD51cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6c2lnbmF0dXJlOkludm9pY2U8L3NiYzpSZWZlcmVuY2VkU2lnbmF0dXJlSUQ+CiAgICAgICAgICAgICAgICAgICAgPGRzOlNpZ25hdHVyZSB4bWxuczpkcz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyIgSWQ9InNpZ25hdHVyZSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxkczpTaWduZWRJbmZvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOkNhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDA2LzEyL3htbC1jMTRuMTEiLz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpTaWduYXR1cmVNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNlY2RzYS1zaGEyNTYiLz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpSZWZlcmVuY2UgSWQ9Imludm9pY2VTaWduZWREYXRhIiBVUkk9IiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlRyYW5zZm9ybXM+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy9UUi8xOTk5L1JFQy14cGF0aC0xOTk5MTExNiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6WFBhdGg+bm90KC8vYW5jZXN0b3Itb3Itc2VsZjo6ZXh0OlVCTEV4dGVuc2lvbnMpPC9kczpYUGF0aD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kczpUcmFuc2Zvcm0+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy9UUi8xOTk5L1JFQy14cGF0aC0xOTk5MTExNiI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6WFBhdGg+bm90KC8vYW5jZXN0b3Itb3Itc2VsZjo6Y2FjOlNpZ25hdHVyZSk8L2RzOlhQYXRoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2RzOlRyYW5zZm9ybT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnL1RSLzE5OTkvUkVDLXhwYXRoLTE5OTkxMTE2Ij4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpYUGF0aD5ub3QoLy9hbmNlc3Rvci1vci1zZWxmOjpjYWM6QWRkaXRpb25hbERvY3VtZW50UmVmZXJlbmNlW2NiYzpJRD0nUVInXSk8L2RzOlhQYXRoPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2RzOlRyYW5zZm9ybT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDYvMTIveG1sLWMxNG4xMSIvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvZHM6VHJhbnNmb3Jtcz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOkRpZ2VzdFZhbHVlPitiQTFtdWNWSTY3SDRXQ2JOL2U5SjJxVXBIVHQzVHdNZHhsa09XVGVvdjg9PC9kczpEaWdlc3RWYWx1ZT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvZHM6UmVmZXJlbmNlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlJlZmVyZW5jZSBUeXBlPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjU2lnbmF0dXJlUHJvcGVydGllcyIgVVJJPSIjeGFkZXNTaWduZWRQcm9wZXJ0aWVzIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOkRpZ2VzdFZhbHVlPlpEWmpNelF5WlRCak5HVmpZMlZsT0RneFlUQmlNemhpTkRGbE0yUXhaVGxrWkRreU1EUTFOVEV3TnpVd04yUmhZalV3TkdObVptTm1OVEZtWTJJMk9BPT08L2RzOkRpZ2VzdFZhbHVlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kczpSZWZlcmVuY2U+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvZHM6U2lnbmVkSW5mbz4KICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlNpZ25hdHVyZVZhbHVlPk1FWUNJUUNZaDVlM2lySXFXbDVZdGFDbktpdWpNSVRtb2tYWU9QTXBJRENJb1dXNzl3SWhBTVhtYytNRkhHdGFlQnNlT3VFR1Rsd0Q2ZzA5Z05RUFJQdVk4OXM2NU9XUzwvZHM6U2lnbmF0dXJlVmFsdWU+CiAgICAgICAgICAgICAgICAgICAgICAgIDxkczpLZXlJbmZvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRzOlg1MDlEYXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpYNTA5Q2VydGlmaWNhdGU+TUlJRDFEQ0NBM21nQXdJQkFnSVRid0FBZTNVQVlWVTM0SS8rNVFBQkFBQjdkVEFLQmdncWhrak9QUVFEQWpCak1SVXdFd1lLQ1pJbWlaUHlMR1FCR1JZRmJHOWpZV3d4RXpBUkJnb0praWFKay9Jc1pBRVpGZ05uYjNZeEZ6QVZCZ29Ka2lhSmsvSXNaQUVaRmdkbGVIUm5ZWHAwTVJ3d0dnWURWUVFERXhOVVUxcEZTVTVXVDBsRFJTMVRkV0pEUVMweE1CNFhEVEl5TURZeE1qRTNOREExTWxvWERUSTBNRFl4TVRFM05EQTFNbG93U1RFTE1Ba0dBMVVFQmhNQ1UwRXhEakFNQmdOVkJBb1RCV0ZuYVd4bE1SWXdGQVlEVlFRTEV3MW9ZWGxoSUhsaFoyaHRiM1Z5TVJJd0VBWURWUVFERXdreE1qY3VNQzR3TGpFd1ZqQVFCZ2NxaGtqT1BRSUJCZ1VyZ1FRQUNnTkNBQVRUQUs5bHJUVmtvOXJrcTZaWWNjOUhEUlpQNGI5UzR6QTRLbTdZWEorc25UVmhMa3pVMEhzbVNYOVVuOGpEaFJUT0hES2FmdDhDL3V1VVk5MzR2dU1ObzRJQ0p6Q0NBaU13Z1lnR0ExVWRFUVNCZ0RCK3BId3dlakViTUJrR0ExVUVCQXdTTVMxb1lYbGhmREl0TWpNMGZETXRNVEV5TVI4d0hRWUtDWkltaVpQeUxHUUJBUXdQTXpBd01EYzFOVGc0TnpBd01EQXpNUTB3Q3dZRFZRUU1EQVF4TVRBd01SRXdEd1lEVlFRYURBaGFZWFJqWVNBeE1qRVlNQllHQTFVRUR3d1BSbTl2WkNCQ2RYTnphVzVsYzNNek1CMEdBMVVkRGdRV0JCU2dtSVdENmJQZmJiS2ttVHdPSlJYdkliSDlIakFmQmdOVkhTTUVHREFXZ0JSMllJejdCcUNzWjFjMW5jK2FyS2NybVRXMUx6Qk9CZ05WSFI4RVJ6QkZNRU9nUWFBL2hqMW9kSFJ3T2k4dmRITjBZM0pzTG5waGRHTmhMbWR2ZGk1ellTOURaWEowUlc1eWIyeHNMMVJUV2tWSlRsWlBTVU5GTFZOMVlrTkJMVEV1WTNKc01JR3RCZ2dyQmdFRkJRY0JBUVNCb0RDQm5UQnVCZ2dyQmdFRkJRY3dBWVppYUhSMGNEb3ZMM1J6ZEdOeWJDNTZZWFJqWVM1bmIzWXVjMkV2UTJWeWRFVnVjbTlzYkM5VVUxcEZhVzUyYjJsalpWTkRRVEV1WlhoMFoyRjZkQzVuYjNZdWJHOWpZV3hmVkZOYVJVbE9WazlKUTBVdFUzVmlRMEV0TVNneEtTNWpjblF3S3dZSUt3WUJCUVVITUFHR0gyaDBkSEE2THk5MGMzUmpjbXd1ZW1GMFkyRXVaMjkyTG5OaEwyOWpjM0F3RGdZRFZSMFBBUUgvQkFRREFnZUFNQjBHQTFVZEpRUVdNQlFHQ0NzR0FRVUZCd01DQmdnckJnRUZCUWNEQXpBbkJna3JCZ0VFQVlJM0ZRb0VHakFZTUFvR0NDc0dBUVVGQndNQ01Bb0dDQ3NHQVFVRkJ3TURNQW9HQ0NxR1NNNDlCQU1DQTBrQU1FWUNJUUNWd0RNY3E2UE8rTWNtc0JYVXovdjFHZGhHcDdycVNhMkF4VEtTdjgzOElBSWhBT0JOREJ0OSszRFNsaWpvVmZ4enJkRGg1MjhXQzM3c21FZG9HV1ZyU3BHMTwvZHM6WDUwOUNlcnRpZmljYXRlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kczpYNTA5RGF0YT4KICAgICAgICAgICAgICAgICAgICAgICAgPC9kczpLZXlJbmZvPgogICAgICAgICAgICAgICAgICAgICAgICA8ZHM6T2JqZWN0PgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPHhhZGVzOlF1YWxpZnlpbmdQcm9wZXJ0aWVzIHhtbG5zOnhhZGVzPSJodHRwOi8vdXJpLmV0c2kub3JnLzAxOTAzL3YxLjMuMiMiIFRhcmdldD0ic2lnbmF0dXJlIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8eGFkZXM6U2lnbmVkUHJvcGVydGllcyBJZD0ieGFkZXNTaWduZWRQcm9wZXJ0aWVzIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHhhZGVzOlNpZ25lZFNpZ25hdHVyZVByb3BlcnRpZXM+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8eGFkZXM6U2lnbmluZ1RpbWU+MjAyMi0wNi0xM1QxMTowNjoxNFo8L3hhZGVzOlNpZ25pbmdUaW1lPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHhhZGVzOlNpZ25pbmdDZXJ0aWZpY2F0ZT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8eGFkZXM6Q2VydD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHhhZGVzOkNlcnREaWdlc3Q+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZHM6RGlnZXN0VmFsdWU+TkRsaVlXWTBZbVZtTnpBeVptRTRPV0l3WkRNellXSXpaakZrT1RZNVl6RmhaalJoWkRFNFpURmtPRGxrTkRZMlkyVXdZekkyTjJReU5EZzBNV1ZsWVE9PTwvZHM6RGlnZXN0VmFsdWU+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwveGFkZXM6Q2VydERpZ2VzdD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHhhZGVzOklzc3VlclNlcmlhbD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpYNTA5SXNzdWVyTmFtZT5DTj1UU1pFSU5WT0lDRS1TdWJDQS0xLCBEQz1leHRnYXp0LCBEQz1nb3YsIERDPWxvY2FsPC9kczpYNTA5SXNzdWVyTmFtZT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkczpYNTA5U2VyaWFsTnVtYmVyPjI0NzUzODI4ODExMzk0NDkwOTQyMDkyMzMwMzI4NDc4Mzg2MzI3MzI1NTYxNDk8L2RzOlg1MDlTZXJpYWxOdW1iZXI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwveGFkZXM6SXNzdWVyU2VyaWFsPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwveGFkZXM6Q2VydD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwveGFkZXM6U2lnbmluZ0NlcnRpZmljYXRlPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3hhZGVzOlNpZ25lZFNpZ25hdHVyZVByb3BlcnRpZXM+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC94YWRlczpTaWduZWRQcm9wZXJ0aWVzPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPC94YWRlczpRdWFsaWZ5aW5nUHJvcGVydGllcz4KICAgICAgICAgICAgICAgICAgICAgICAgPC9kczpPYmplY3Q+CiAgICAgICAgICAgICAgICAgICAgPC9kczpTaWduYXR1cmU+CiAgICAgICAgICAgICAgICA8L3NhYzpTaWduYXR1cmVJbmZvcm1hdGlvbj4KICAgICAgICAgICAgPC9zaWc6VUJMRG9jdW1lbnRTaWduYXR1cmVzPgogICAgICAgIDwvZXh0OkV4dGVuc2lvbkNvbnRlbnQ+CiAgICA8L2V4dDpVQkxFeHRlbnNpb24+CjwvZXh0OlVCTEV4dGVuc2lvbnM+CiAgICAKICAgIDxjYmM6UHJvZmlsZUlEPnJlcG9ydGluZzoxLjA8L2NiYzpQcm9maWxlSUQ+CiAgICA8Y2JjOklEPlNNRTAwMDYyPC9jYmM6SUQ+CiAgICA8Y2JjOlVVSUQ+NmY0ZDIwZTAtNmJmZS00YTgwLTkzODktN2RhYmU2NjIwZjEyPC9jYmM6VVVJRD4KICAgIDxjYmM6SXNzdWVEYXRlPjIwMjItMDMtMTM8L2NiYzpJc3N1ZURhdGU+CiAgICA8Y2JjOklzc3VlVGltZT4xNDo0MDo0MDwvY2JjOklzc3VlVGltZT4KICAgIDxjYmM6SW52b2ljZVR5cGVDb2RlIG5hbWU9IjAyMTEwMTAiPjM4ODwvY2JjOkludm9pY2VUeXBlQ29kZT4KICAgIDxjYmM6RG9jdW1lbnRDdXJyZW5jeUNvZGU+U0FSPC9jYmM6RG9jdW1lbnRDdXJyZW5jeUNvZGU+CiAgICA8Y2JjOlRheEN1cnJlbmN5Q29kZT5TQVI8L2NiYzpUYXhDdXJyZW5jeUNvZGU+CiAgICA8Y2FjOkFkZGl0aW9uYWxEb2N1bWVudFJlZmVyZW5jZT4KICAgICAgICA8Y2JjOklEPklDVjwvY2JjOklEPgogICAgICAgIDxjYmM6VVVJRD42MjwvY2JjOlVVSUQ+CiAgICA8L2NhYzpBZGRpdGlvbmFsRG9jdW1lbnRSZWZlcmVuY2U+CiAgICA8Y2FjOkFkZGl0aW9uYWxEb2N1bWVudFJlZmVyZW5jZT4KICAgICAgICA8Y2JjOklEPlBJSDwvY2JjOklEPgogICAgICAgIDxjYWM6QXR0YWNobWVudD4KICAgICAgICAgICAgPGNiYzpFbWJlZGRlZERvY3VtZW50QmluYXJ5T2JqZWN0IG1pbWVDb2RlPSJ0ZXh0L3BsYWluIj5OV1psWTJWaU5qWm1abU00Tm1Zek9HUTVOVEkzT0Raak5tUTJPVFpqTnpsak1tUmlZekl6T1dSa05HVTVNV0kwTmpjeU9XUTNNMkV5TjJaaU5UZGxPUT09PC9jYmM6RW1iZWRkZWREb2N1bWVudEJpbmFyeU9iamVjdD4KICAgICAgICA8L2NhYzpBdHRhY2htZW50PgogICAgPC9jYWM6QWRkaXRpb25hbERvY3VtZW50UmVmZXJlbmNlPgogICAgCiAgICAKICAgIDxjYWM6QWRkaXRpb25hbERvY3VtZW50UmVmZXJlbmNlPgogICAgICAgIDxjYmM6SUQ+UVI8L2NiYzpJRD4KICAgICAgICA8Y2FjOkF0dGFjaG1lbnQ+CiAgICAgICAgICAgIDxjYmM6RW1iZWRkZWREb2N1bWVudEJpbmFyeU9iamVjdCBtaW1lQ29kZT0idGV4dC9wbGFpbiI+QVJkQmFHMWxaQ0JOYjJoaGJXVmtJRUZNSUVGb2JXRmtlUUlQTXpBd01EYzFOVGc0TnpBd01EQXpBeFF5TURJeUxUQXpMVEV6VkRFME9qUXdPalF3V2dRSE1URXdPQzQ1TUFVRk1UUTBMamtHTEN0aVFURnRkV05XU1RZM1NEUlhRMkpPTDJVNVNqSnhWWEJJVkhRelZIZE5aSGhzYTA5WFZHVnZkamc5QjJCTlJWbERTVkZEV1dnMVpUTnBja2x4VjJ3MVdYUmhRMjVMYVhWcVRVbFViVzlyV0ZsUFVFMXdTVVJEU1c5WFZ6YzVkMGxvUVUxWWJXTXJUVVpJUjNSaFpVSnpaVTkxUlVkVWJIZEVObWN3T1dkT1VWQlNVSFZaT0Rsek5qVlBWMU1JV0RCV01CQUdCeXFHU000OUFnRUdCU3VCQkFBS0EwSUFCTk1BcjJXdE5XU2oydVNycGxoeHowY05Gay9odjFMak1EZ3FidGhjbjZ5ZE5XRXVUTlRRZXlaSmYxU2Z5TU9GRk00Y01wcCszd0wrNjVSajNmaSs0dzBKU0RCR0FpRUFsY0F6SEt1anp2akhKckFWMU0vNzlSbllScWU2NmttdGdNVXlrci9OL0NBQ0lRRGdUUXdiZmZ0dzBwWW82Rlg4YzYzUTRlZHZGZ3QrN0poSGFCbGxhMHFSdFE9PTwvY2JjOkVtYmVkZGVkRG9jdW1lbnRCaW5hcnlPYmplY3Q+CiAgICAgICAgPC9jYWM6QXR0YWNobWVudD4KPC9jYWM6QWRkaXRpb25hbERvY3VtZW50UmVmZXJlbmNlPjxjYWM6U2lnbmF0dXJlPgogICAgICA8Y2JjOklEPnVybjpvYXNpczpuYW1lczpzcGVjaWZpY2F0aW9uOnVibDpzaWduYXR1cmU6SW52b2ljZTwvY2JjOklEPgogICAgICA8Y2JjOlNpZ25hdHVyZU1ldGhvZD51cm46b2FzaXM6bmFtZXM6c3BlY2lmaWNhdGlvbjp1Ymw6ZHNpZzplbnZlbG9wZWQ6eGFkZXM8L2NiYzpTaWduYXR1cmVNZXRob2Q+CjwvY2FjOlNpZ25hdHVyZT48Y2FjOkFjY291bnRpbmdTdXBwbGllclBhcnR5PgogICAgICAgIDxjYWM6UGFydHk+CiAgICAgICAgICAgIDxjYWM6UGFydHlJZGVudGlmaWNhdGlvbj4KICAgICAgICAgICAgICAgIDxjYmM6SUQgc2NoZW1lSUQ9IkNSTiI+NDU0NjM0NjQ1NjQ1NjU0PC9jYmM6SUQ+CiAgICAgICAgICAgIDwvY2FjOlBhcnR5SWRlbnRpZmljYXRpb24+CiAgICAgICAgICAgIDxjYWM6UG9zdGFsQWRkcmVzcz4KICAgICAgICAgICAgICAgIDxjYmM6U3RyZWV0TmFtZT50ZXN0PC9jYmM6U3RyZWV0TmFtZT4KICAgICAgICAgICAgICAgIDxjYmM6QnVpbGRpbmdOdW1iZXI+MzQ1NDwvY2JjOkJ1aWxkaW5nTnVtYmVyPgogICAgICAgICAgICAgICAgPGNiYzpQbG90SWRlbnRpZmljYXRpb24+MTIzNDwvY2JjOlBsb3RJZGVudGlmaWNhdGlvbj4KICAgICAgICAgICAgICAgIDxjYmM6Q2l0eVN1YmRpdmlzaW9uTmFtZT5mZ2ZmPC9jYmM6Q2l0eVN1YmRpdmlzaW9uTmFtZT4KICAgICAgICAgICAgICAgIDxjYmM6Q2l0eU5hbWU+Uml5YWRoPC9jYmM6Q2l0eU5hbWU+CiAgICAgICAgICAgICAgICA8Y2JjOlBvc3RhbFpvbmU+MTIzNDU8L2NiYzpQb3N0YWxab25lPgogICAgICAgICAgICAgICAgPGNiYzpDb3VudHJ5U3ViZW50aXR5PnRlc3Q8L2NiYzpDb3VudHJ5U3ViZW50aXR5PgogICAgICAgICAgICAgICAgPGNhYzpDb3VudHJ5PgogICAgICAgICAgICAgICAgICAgIDxjYmM6SWRlbnRpZmljYXRpb25Db2RlPlNBPC9jYmM6SWRlbnRpZmljYXRpb25Db2RlPgogICAgICAgICAgICAgICAgPC9jYWM6Q291bnRyeT4KICAgICAgICAgICAgPC9jYWM6UG9zdGFsQWRkcmVzcz4KICAgICAgICAgICAgPGNhYzpQYXJ0eVRheFNjaGVtZT4KICAgICAgICAgICAgICAgIDxjYmM6Q29tcGFueUlEPjMwMDA3NTU4ODcwMDAwMzwvY2JjOkNvbXBhbnlJRD4KICAgICAgICAgICAgICAgIDxjYWM6VGF4U2NoZW1lPgogICAgICAgICAgICAgICAgICAgIDxjYmM6SUQ+VkFUPC9jYmM6SUQ+CiAgICAgICAgICAgICAgICA8L2NhYzpUYXhTY2hlbWU+CiAgICAgICAgICAgIDwvY2FjOlBhcnR5VGF4U2NoZW1lPgogICAgICAgICAgICA8Y2FjOlBhcnR5TGVnYWxFbnRpdHk+CiAgICAgICAgICAgICAgICA8Y2JjOlJlZ2lzdHJhdGlvbk5hbWU+QWhtZWQgTW9oYW1lZCBBTCBBaG1hZHk8L2NiYzpSZWdpc3RyYXRpb25OYW1lPgogICAgICAgICAgICA8L2NhYzpQYXJ0eUxlZ2FsRW50aXR5PgogICAgICAgIDwvY2FjOlBhcnR5PgogICAgPC9jYWM6QWNjb3VudGluZ1N1cHBsaWVyUGFydHk+CiAgICA8Y2FjOkFjY291bnRpbmdDdXN0b21lclBhcnR5PgogICAgICAgIDxjYWM6UGFydHk+CiAgICAgICAgICAgIDxjYWM6UGFydHlJZGVudGlmaWNhdGlvbj4KICAgICAgICAgICAgICAgIDxjYmM6SUQgc2NoZW1lSUQ9Ik5BVCI+MjM0NTwvY2JjOklEPgogICAgICAgICAgICA8L2NhYzpQYXJ0eUlkZW50aWZpY2F0aW9uPgogICAgICAgICAgICA8Y2FjOlBvc3RhbEFkZHJlc3M+CiAgICAgICAgICAgICAgICA8Y2JjOlN0cmVldE5hbWU+YmFhb3VuPC9jYmM6U3RyZWV0TmFtZT4KICAgICAgICAgICAgICAgIDxjYmM6QWRkaXRpb25hbFN0cmVldE5hbWU+c2RzZDwvY2JjOkFkZGl0aW9uYWxTdHJlZXROYW1lPgogICAgICAgICAgICAgICAgPGNiYzpCdWlsZGluZ051bWJlcj4zMzUzPC9jYmM6QnVpbGRpbmdOdW1iZXI+CiAgICAgICAgICAgICAgICA8Y2JjOlBsb3RJZGVudGlmaWNhdGlvbj4zNDM0PC9jYmM6UGxvdElkZW50aWZpY2F0aW9uPgogICAgICAgICAgICAgICAgPGNiYzpDaXR5U3ViZGl2aXNpb25OYW1lPmZnZmY8L2NiYzpDaXR5U3ViZGl2aXNpb25OYW1lPgogICAgICAgICAgICAgICAgPGNiYzpDaXR5TmFtZT5EaHVybWE8L2NiYzpDaXR5TmFtZT4KICAgICAgICAgICAgICAgIDxjYmM6UG9zdGFsWm9uZT4zNDUzNDwvY2JjOlBvc3RhbFpvbmU+CiAgICAgICAgICAgICAgICA8Y2JjOkNvdW50cnlTdWJlbnRpdHk+dWxoazwvY2JjOkNvdW50cnlTdWJlbnRpdHk+CiAgICAgICAgICAgICAgICA8Y2FjOkNvdW50cnk+CiAgICAgICAgICAgICAgICAgICAgPGNiYzpJZGVudGlmaWNhdGlvbkNvZGU+U0E8L2NiYzpJZGVudGlmaWNhdGlvbkNvZGU+CiAgICAgICAgICAgICAgICA8L2NhYzpDb3VudHJ5PgogICAgICAgICAgICA8L2NhYzpQb3N0YWxBZGRyZXNzPgogICAgICAgICAgICA8Y2FjOlBhcnR5VGF4U2NoZW1lPgogICAgICAgICAgICAgICAgPGNhYzpUYXhTY2hlbWU+CiAgICAgICAgICAgICAgICAgICAgPGNiYzpJRD5WQVQ8L2NiYzpJRD4KICAgICAgICAgICAgICAgIDwvY2FjOlRheFNjaGVtZT4KICAgICAgICAgICAgPC9jYWM6UGFydHlUYXhTY2hlbWU+CiAgICAgICAgICAgIDxjYWM6UGFydHlMZWdhbEVudGl0eT4KICAgICAgICAgICAgICAgIDxjYmM6UmVnaXN0cmF0aW9uTmFtZT5zZHNhPC9jYmM6UmVnaXN0cmF0aW9uTmFtZT4KICAgICAgICAgICAgPC9jYWM6UGFydHlMZWdhbEVudGl0eT4KICAgICAgICA8L2NhYzpQYXJ0eT4KICAgIDwvY2FjOkFjY291bnRpbmdDdXN0b21lclBhcnR5PgogICAgPGNhYzpEZWxpdmVyeT4KICAgICAgICA8Y2JjOkFjdHVhbERlbGl2ZXJ5RGF0ZT4yMDIyLTAzLTEzPC9jYmM6QWN0dWFsRGVsaXZlcnlEYXRlPgogICAgICAgIDxjYmM6TGF0ZXN0RGVsaXZlcnlEYXRlPjIwMjItMDMtMTU8L2NiYzpMYXRlc3REZWxpdmVyeURhdGU+CiAgICA8L2NhYzpEZWxpdmVyeT4KICAgIDxjYWM6UGF5bWVudE1lYW5zPgogICAgICAgIDxjYmM6UGF5bWVudE1lYW5zQ29kZT4xMDwvY2JjOlBheW1lbnRNZWFuc0NvZGU+CiAgICA8L2NhYzpQYXltZW50TWVhbnM+CiAgICA8Y2FjOkFsbG93YW5jZUNoYXJnZT4KICAgICAgICA8Y2JjOklEPjE8L2NiYzpJRD4KICAgICAgICA8Y2JjOkNoYXJnZUluZGljYXRvcj5mYWxzZTwvY2JjOkNoYXJnZUluZGljYXRvcj4KICAgICAgICA8Y2JjOkFsbG93YW5jZUNoYXJnZVJlYXNvbj5kaXNjb3VudDwvY2JjOkFsbG93YW5jZUNoYXJnZVJlYXNvbj4KICAgICAgICA8Y2JjOkFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjI8L2NiYzpBbW91bnQ+CiAgICAgICAgPGNhYzpUYXhDYXRlZ29yeT4KICAgICAgICAgICAgPGNiYzpJRCBzY2hlbWVBZ2VuY3lJRD0iNiIgc2NoZW1lSUQ9IlVOL0VDRSA1MzA1Ij5TPC9jYmM6SUQ+CiAgICAgICAgICAgIDxjYmM6UGVyY2VudD4xNTwvY2JjOlBlcmNlbnQ+CiAgICAgICAgICAgIDxjYWM6VGF4U2NoZW1lPgogICAgICAgICAgICAgICAgPGNiYzpJRCBzY2hlbWVBZ2VuY3lJRD0iNiIgc2NoZW1lSUQ9IlVOL0VDRSA1MTUzIj5WQVQ8L2NiYzpJRD4KICAgICAgICAgICAgPC9jYWM6VGF4U2NoZW1lPgogICAgICAgIDwvY2FjOlRheENhdGVnb3J5PgogICAgPC9jYWM6QWxsb3dhbmNlQ2hhcmdlPgogICAgPGNhYzpUYXhUb3RhbD4KICAgICAgICA8Y2JjOlRheEFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjE0NC45PC9jYmM6VGF4QW1vdW50PgogICAgICAgIDxjYWM6VGF4U3VidG90YWw+CiAgICAgICAgICAgIDxjYmM6VGF4YWJsZUFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjk2Ni4wMDwvY2JjOlRheGFibGVBbW91bnQ+CiAgICAgICAgICAgIDxjYmM6VGF4QW1vdW50IGN1cnJlbmN5SUQ9IlNBUiI+MTQ0LjkwPC9jYmM6VGF4QW1vdW50PgogICAgICAgICAgICA8Y2FjOlRheENhdGVnb3J5PgogICAgICAgICAgICAgICAgPGNiYzpJRCBzY2hlbWVBZ2VuY3lJRD0iNiIgc2NoZW1lSUQ9IlVOL0VDRSA1MzA1Ij5TPC9jYmM6SUQ+CiAgICAgICAgICAgICAgICA8Y2JjOlBlcmNlbnQ+MTUuMDA8L2NiYzpQZXJjZW50PgogICAgICAgICAgICAgICAgPGNhYzpUYXhTY2hlbWU+CiAgICAgICAgICAgICAgICAgICAgPGNiYzpJRCBzY2hlbWVBZ2VuY3lJRD0iNiIgc2NoZW1lSUQ9IlVOL0VDRSA1MTUzIj5WQVQ8L2NiYzpJRD4KICAgICAgICAgICAgICAgIDwvY2FjOlRheFNjaGVtZT4KICAgICAgICAgICAgPC9jYWM6VGF4Q2F0ZWdvcnk+CiAgICAgICAgPC9jYWM6VGF4U3VidG90YWw+CiAgICA8L2NhYzpUYXhUb3RhbD4KICAgIDxjYWM6VGF4VG90YWw+CiAgICAgICAgPGNiYzpUYXhBbW91bnQgY3VycmVuY3lJRD0iU0FSIj4xNDQuOTwvY2JjOlRheEFtb3VudD4KCiAgICA8L2NhYzpUYXhUb3RhbD4KICAgIDxjYWM6TGVnYWxNb25ldGFyeVRvdGFsPgogICAgICAgIDxjYmM6TGluZUV4dGVuc2lvbkFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjk2Ni4wMDwvY2JjOkxpbmVFeHRlbnNpb25BbW91bnQ+CiAgICAgICAgPGNiYzpUYXhFeGNsdXNpdmVBbW91bnQgY3VycmVuY3lJRD0iU0FSIj45NjQuMDA8L2NiYzpUYXhFeGNsdXNpdmVBbW91bnQ+CiAgICAgICAgPGNiYzpUYXhJbmNsdXNpdmVBbW91bnQgY3VycmVuY3lJRD0iU0FSIj4xMTA4LjkwPC9jYmM6VGF4SW5jbHVzaXZlQW1vdW50PgogICAgICAgIDxjYmM6QWxsb3dhbmNlVG90YWxBbW91bnQgY3VycmVuY3lJRD0iU0FSIj4yLjAwPC9jYmM6QWxsb3dhbmNlVG90YWxBbW91bnQ+CiAgICAgICAgPGNiYzpQcmVwYWlkQW1vdW50IGN1cnJlbmN5SUQ9IlNBUiI+MC4wMDwvY2JjOlByZXBhaWRBbW91bnQ+CiAgICAgICAgPGNiYzpQYXlhYmxlQW1vdW50IGN1cnJlbmN5SUQ9IlNBUiI+MTEwOC45MDwvY2JjOlBheWFibGVBbW91bnQ+CiAgICA8L2NhYzpMZWdhbE1vbmV0YXJ5VG90YWw+CiAgICA8Y2FjOkludm9pY2VMaW5lPgogICAgICAgIDxjYmM6SUQ+MTwvY2JjOklEPgogICAgICAgIDxjYmM6SW52b2ljZWRRdWFudGl0eSB1bml0Q29kZT0iUENFIj40NC4wMDAwMDA8L2NiYzpJbnZvaWNlZFF1YW50aXR5PgogICAgICAgIDxjYmM6TGluZUV4dGVuc2lvbkFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjk2Ni4wMDwvY2JjOkxpbmVFeHRlbnNpb25BbW91bnQ+CiAgICAgICAgPGNhYzpUYXhUb3RhbD4KICAgICAgICAgICAgPGNiYzpUYXhBbW91bnQgY3VycmVuY3lJRD0iU0FSIj4xNDQuOTA8L2NiYzpUYXhBbW91bnQ+CiAgICAgICAgICAgIDxjYmM6Um91bmRpbmdBbW91bnQgY3VycmVuY3lJRD0iU0FSIj4xMTEwLjkwPC9jYmM6Um91bmRpbmdBbW91bnQ+CgogICAgICAgIDwvY2FjOlRheFRvdGFsPgogICAgICAgIDxjYWM6SXRlbT4KICAgICAgICAgICAgPGNiYzpOYW1lPmRzZDwvY2JjOk5hbWU+CiAgICAgICAgICAgIDxjYWM6Q2xhc3NpZmllZFRheENhdGVnb3J5PgogICAgICAgICAgICAgICAgPGNiYzpJRD5TPC9jYmM6SUQ+CiAgICAgICAgICAgICAgICA8Y2JjOlBlcmNlbnQ+MTUuMDA8L2NiYzpQZXJjZW50PgogICAgICAgICAgICAgICAgPGNhYzpUYXhTY2hlbWU+CiAgICAgICAgICAgICAgICAgICAgPGNiYzpJRD5WQVQ8L2NiYzpJRD4KICAgICAgICAgICAgICAgIDwvY2FjOlRheFNjaGVtZT4KICAgICAgICAgICAgPC9jYWM6Q2xhc3NpZmllZFRheENhdGVnb3J5PgogICAgICAgIDwvY2FjOkl0ZW0+CiAgICAgICAgPGNhYzpQcmljZT4KICAgICAgICAgICAgPGNiYzpQcmljZUFtb3VudCBjdXJyZW5jeUlEPSJTQVIiPjIyLjAwPC9jYmM6UHJpY2VBbW91bnQ+CiAgICAgICAgICAgIDxjYWM6QWxsb3dhbmNlQ2hhcmdlPgogICAgICAgICAgICAgICAgPGNiYzpDaGFyZ2VJbmRpY2F0b3I+ZmFsc2U8L2NiYzpDaGFyZ2VJbmRpY2F0b3I+CiAgICAgICAgICAgICAgICA8Y2JjOkFsbG93YW5jZUNoYXJnZVJlYXNvbj5kaXNjb3VudDwvY2JjOkFsbG93YW5jZUNoYXJnZVJlYXNvbj4KICAgICAgICAgICAgICAgIDxjYmM6QW1vdW50IGN1cnJlbmN5SUQ9IlNBUiI+Mi4wMDwvY2JjOkFtb3VudD4KICAgICAgICAgICAgPC9jYWM6QWxsb3dhbmNlQ2hhcmdlPgogICAgICAgIDwvY2FjOlByaWNlPgogICAgPC9jYWM6SW52b2ljZUxpbmU+CjwvSW52b2ljZT4="}
        if type == "1":
            return requests.post("https://gw-apic-gov.gazt.gov.sa/e-invoicing/developer-portal/invoices/reporting/single",
                                 data=json.dumps(data, ensure_ascii=False), headers=headers)
            
        elif type == "2":
            return requests.post("https://gw-apic-gov.gazt.gov.sa/e-invoicing/developer-portal/invoices/clearance/single",
                                 data=json.dumps(data, ensure_ascii=False), headers=headers)
            
        elif type == "3" or type == "6":
            data = {
                "csr": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQnl6Q0NBWElDQVFBd1R6RUxNQWtHQTFVRUJoTUNVMEV4RnpBVkJnTlZCQXNNRG1GdGJXRnVJRUp5WVc1agphR05vTVJNd0VRWURWUVFLREFwb1lYbGhJSGxoWnlBek1SSXdFQVlEVlFRRERBa3hNamN1TUM0d0xqRXdWakFRCkJnY3Foa2pPUFFJQkJnVXJnUVFBQ2dOQ0FBVGJpclluL3l2L09zSGhGbE1QdkZjUnhJM250dWsxaXd0aWxOWXUKVjIrOTVrbkRBc2hiNU9Gc0lZQ0hvL2tMMDBLdnhMczQrcytyMWc4dnFVZ3BvazhYb0lIRE1JSEFCZ2txaGtpRwo5dzBCQ1E0eGdiSXdnYTh3SkFZSkt3WUJCQUdDTnhRQ0JCY1RGVlJUVkZwQlZFTkJMVU52WkdVdFUybG5ibWx1Clp6Q0JoZ1lEVlIwUkJIOHdmYVI3TUhreEd6QVpCZ05WQkFRTUVqRXRhR0Y1WVh3eUxUSXpOSHd6TFRNMU5ERWYKTUIwR0NnbVNKb21UOGl4a0FRRU1Eek14TURFM05UTTVOelF3TURBd016RU5NQXNHQTFVRURBd0VNVEV3TURFUQpNQTRHQTFVRUdnd0hXbUYwWTJFZ016RVlNQllHQTFVRUR3d1BSbTl2WkNCQ2RYTnphVzVsYzNNek1Bb0dDQ3FHClNNNDlCQU1DQTBjQU1FUUNJQ3JyTzdtSzZWZTZNTmIrSlNJRkRmK0FGMjhqV2ZJYTNIdzlhWEdVOS9KbkFpQXIKSnBVc0h4Z1RrOGtQZTRQSnNJVGJJYXlTeUh2emZwdHFFTWZEajdQN2F3PT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0t"
            }
            headers['OTP']='123345'
            return requests.post("https://gw-apic-gov.gazt.gov.sa/e-invoicing/developer-portal/compliance",
                                 data=json.dumps(data, ensure_ascii=False), headers=headers)
            
        elif type == "4":
            return requests.post("https://gw-apic-gov.gazt.gov.sa/e-invoicing/developer-portal/compliance/invoices",data=json.dumps(data,       ensure_ascii=False), headers=headers)
            
        elif type == "5":
            data = {
                "compliance_request_id": "1234567890123"
            }
            return requests.post("https://gw-apic-gov.gazt.gov.sa/e-invoicing/developer-portal/production/csids",
                                 data=json.dumps(data, ensure_ascii=False), headers=headers)
        else:
            return None