from rest_framework import views
from rest_framework.response import Response

from apps.common.models import *

class ChangeCompanyName(views.APIView):
    def post(self, request, *args, **kwargs):
        item_id = request.data.get('item')    
        item = Item.objects.get(id=item_id)
        
        company = item.company.values()
        company = list(company)
        return Response({"data": company})
    
class ChangeCompanyNameAndFRC(views.APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        company = Company.objects.get(
            id=request.data.get('company'),
        )
        
        frc_plans = company.frc_plans.values()
        frc_plans = list(frc_plans)
        print(frc_plans)
        return Response(
            {   
                'frc_plans': frc_plans
            },
        )
    
