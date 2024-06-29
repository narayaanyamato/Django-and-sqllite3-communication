from django.shortcuts import render
from modelapp1.models import Student
# Create your views here.
def showrec(request):
    data=Student.objects.all()
    std_rec={"data":data}
    return render(request,'Pages/stdrec.html',std_rec)