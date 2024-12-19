from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.db.models import Sum

# Create your views here.

class PlaceOrderView(APIView):
    # def get(self, request):
    #     return Response({"error": "GET method is not allowed on this endpoint."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            product=Product.objects.filter(product_id=request.data['product_id']).first()
            if not product:
                return Response({"error":"Invalid product id"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"status":"success","message":"Order Placed Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModifyOrderView(APIView):
    def put(self,request,order_id):
        try:
            order=Order.objects.get(order_id=order_id)
            if order.status in ['delivered','cancled']:
                return Response({"error":"Cannot Modify Delivered or canceled order"})
            serializer=OrderUpdateSerializer(order ,data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"success","message":"Order Updated Successfully!"})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"error":"Order Not Found"},status=status.HTTP_404_NOT_FOUND)
        
class CancelOrderView(APIView):
    def delete(self,request,order_id):
        try:
            order=Order.objects.get(order_id=order_id)
            if order.status == 'delivered':
                return Response({"error":"Delivered Order can not be Canceled"},status=status.HTTP_400_BAD_REQUEST)
            order.status='canceled'
            order.save()
            return Response({"status":"success","message":"Order Has been Canceled!"})
        except Order.DoesNotExist:
            return Response({"error":"Order not Found"},status=status.HTTP_404_NOT_FOUND)
        
class CalculateTotalView(APIView):
    def get(self,request,customer_id):
        orders=Order.objects.filter(customer_id=customer_id,status__in=['placed','processed'])
        total_amount=orders.aggregate(Sum('price'))['price__sum'] or 0
        discount=0.1 if total_amount>5000 else 0
        final_total=total_amount *(1-discount)

        return Response({
            "customer_id":customer_id,
            "total_amount":total_amount,
            "discount":f"{int(discount*100)}%",
            "final_total":final_total

        })