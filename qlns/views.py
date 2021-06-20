from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NhanvienSerializer
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import Changeformnhanvien
# Create your views here.
class Index(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self,request):
        nv = Nhanvien.objects.all()
        us = User.objects.all()
         

        return render(request,'index.html')

class Login(View):

    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user=user)
            return redirect('index')
        else:
            return render(request,'login.html')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class Giaoviec(View):
    def get(self,request):
        return render(request,'kanban.html')
class Nhanvientotal(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        nv= Nhanvien.objects.all()

        return render(request, 'nhanvien.html',{'nv':nv})

    def post(self,request):
        if request.method == 'POST':

            manv = request.POST.get('manv')
            tennv= request.POST.get('tennv')
            username = User.objects.get(id=2)
            ngaysinh= request.POST.get('ngaysinh')
            diachi= request.POST.get('diachi')
            quequan= request.POST.get('quequan')
            cmnd = request.POST.get('cmnd')
            cmnd_1 =request.FILES['cmndmt']

            cmnd_2 =request.FILES['cmndms']
            avatar =request.FILES['avatar']
            sdt = request.POST.get('sdt')
            line = request.POST.get('line')
            email = request.POST.get('email')
            Nhanvien.objects.create(manv=manv,tennv=tennv,username=username,ngaysinh=ngaysinh,
                                    diachi=diachi, quequan=quequan, cmnd=cmnd,cmnd_1=cmnd_1,
                                    cmnd_2=cmnd_2,avatar=avatar,sdt=sdt,line=line,email=email)
            nv = Nhanvien.objects.all()

            context ={
                'ms':'them thanh cong',
                'nv':nv
            }
            messages.success(request, 'Thêm Thành Cong')
            return redirect('nhanvien')

class Getnhanvien(APIView):

    def get(self,request):
        nv = Nhanvien.objects.all()
        NhanvienSerializer(nv,many=True)
        return Response(nv.data)


class Viewnhanvien(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        return redirect('nhanvien')
    def post(self,request):

        nv = Nhanvien.objects.get(id=request.POST.get('idview'))
        context ={
            'nv':nv
        }
        return render(request,'viewnhanvien.html',context)


class Profile(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        id = user.id
        nv = Nhanvien.objects.get(username=id)
        idnv = nv.id
        nv =Nhanvien.objects.get(pk=idnv)

        try:
            hsld = Hosonhanvien.objects.get(nhanvien=nv.id)
            now_year = datetime.datetime.now().year - hsld.ngaychinhthuc.year

        except Hosonhanvien.DoesNotExist:
            hsld = {'id':'Đang cập nhật','masobh':'Đang cập nhật'}
            now_year="Đang Cập Nhật Số "
        context = {
            'nv': nv,
            'id': id,
            'hsld': hsld,
            'now': now_year
        }
        return render(request,'profile.html',context)



class Dsnhanvien(LoginRequiredMixin,View):
    login_url = "login/"
    def get(self,request):
        nv = Nhanvien.objects.all()
        pb = Phongban.objects.get(tenpb = "BÁN SỈ")
        idbs = pb.id

        nvbs = Nhanvien.objects.filter(phongban=idbs)
        nvhcns = Nhanvien.objects.filter(phongban=2)#HCNS
        nvkt = Nhanvien.objects.filter(phongban=1)
        nvit = Nhanvien.objects.filter(phongban=3)
        context={
            'nv':nv,
            'nvhcns':nvhcns,
            'nvkt':nvkt,
            'nvbs':nvbs,
            'nvit':nvit,

        }
        return render(request,'dsnhanvien.html',context)

    def post(self, request):
        tennhanvien = request.POST.get('tennhanvien')
        nvsearch = Nhanvien.objects.filter(tennv__icontains=tennhanvien)
        context = {
            'nvsearch': nvsearch,
        }
        return render(request, 'dsnhanvien.html', context)


class Changenhanvien(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self,request,nhanvien_id):
        nv = Nhanvien.objects.get(id=nhanvien_id)

        try:
            hsld = Hosonhanvien.objects.get(nhanvien=nv.id)
            now_year = datetime.datetime.now().year - hsld.ngaychinhthuc.year

        except Hosonhanvien.DoesNotExist:
            hsld = {'id':'Đang cập nhật','masobh':'Đang cập nhật'}
            now_year="Đang Cập Nhật Số "
        context={
                'nv': nv,
                'id': nhanvien_id,
                'hsld': hsld,
                'now': now_year
            }

        return render(request, 'xemnhanvien.html', context)

    def post(self,request,nhanvien_id):
        if request.method == 'POST':
            form = Nhanvien.objects.get(id=nhanvien_id)

            form = Changeformnhanvien(request.POST, request.FILES , instance=form)


            if request.POST['change']:
                if form.is_valid():
                    form.save()

        return redirect('nhanvien')


class Deletenhanvien(View):
    def get(self,request,nhanvien_id):
        form = Nhanvien.objects.get(id=nhanvien_id)
        form.delete()
        return redirect('nhanvien')


class Phieuluongupload(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self,request):
        pl = Phieuluong_upload.objects.all()
        context ={
            'pl':pl,
            'thang':[1,2,3,4,5,6,7,8,9,10,11,12],
            'nam':[2021,2022,2023],
        }
        return render(request,'phieuluongupload.html',context)

    def post(self,request):
        thang = request.POST.get('thang')
        nam = request.POST.get('nam')
        try:

            pl = Phieuluong_upload.objects.filter(thang=thang,nam=nam)

        except Phieuluong_upload.DoesNotExist:
            pl = Phieuluong_upload.objects.all()


        context = {
            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020,2021, 2022, 2023],
        }
        return render(request,'phieuluongupload.html',context)

class Phieuluongcanhan(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self,request,nhanvien_id):
        pl = Phieuluong_upload.objects.filter(pk=nhanvien_id)

        context = {
            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],

        }
        return render(request, 'phieuluongcanhan.html', context)


class Phieuluonguser(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self,request):
        user = request.user
        id = user.id
        nv = Nhanvien.objects.get(username=id)
        idnv =nv.id

        pl = Phieuluong_upload.objects.filter(nhanvien=idnv).order_by('-nam','-thang')
        context={
            'user':user,
             'pl':pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],
        }


        return render(request,'phieuluonguser.html',context)

    def post(self,request):
        nam = request.POST.get('nam')
        thang = request.POST.get('thang')
        if nam == 100 and thang == 100:
            messages.error(request,"Chọn Tháng Năm Để Loc")
        else:
            user = request.user
            id = user.id
            nv = Nhanvien.objects.get(username=id)
            idnv = nv.id

        pl = Phieuluong_upload.objects.filter(nhanvien=idnv, nam=nam, thang=thang)
        context = {

            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],
        }

        return render(request, 'phieuluonguser.html', context)

class Thoiviecnhanvien(View):
    pass


class Delete_checkbox(View):
    def get(seft,request):
        all = Nhanvien.objects.all()
        context={
            'nv':all
        }
        return render(request, 'deletenhanvien.html',context)
    def post(self,request):
        if request.method == "POST":
            print("HElLo")



        return redirect('nhanvien')
