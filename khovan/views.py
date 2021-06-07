from time import sleep

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from qlns.models import Nhanvien
from django.http import HttpResponse, response
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail


# Create your views here.
class Nhaphangs(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        hanghoa = Hanghoa.objects.all()
        khohang = Khohang.objects.all()
        pnh_nonactive = Phieunhaphang.objects.filter(tinhtrang=False,tuchoi=False)
        pnh_disable = Phieunhaphang.objects.filter(tinhtrang=False,tuchoi=True)
        pnh_active = Phieunhaphang.objects.filter(tinhtrang=True,tuchoi=False)

        context = {
            'hanghoa': hanghoa,
            'khohang': khohang,
            'pnh_nonactive': pnh_nonactive,
            'pnh_active': pnh_active,
            'pnh_disable':pnh_disable,
        }
        return render(request, 'nhaphang.html', context)


class Phieunhapkho(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):

        hangsx = Hangsx.objects.all()
        hanghoa = Hanghoa.objects.all()
        khohang = Khohang.objects.all()
        thukho = Thukho_Khohang.objects.all()
        nhanvien = Nhanvien.objects.filter(username=request.user, phongban=3)
        nhancungcap = Nhacungcap.objects.all()
        k = Phieunhaphang.objects.all()
        sum_i = 0
        if k:
            for item in k:
                sum_i = item.id + 1

        else:
            sum_i = 1

        context = {
            'hangsx': hangsx,
            'hanghoa': hanghoa,
            'khohang': khohang,
            'thukho': thukho,
            'nhanvien': nhanvien,
            'nhancungcap': nhancungcap,
            'code': sum_i,
        }
        return render(request, 'phieunhapkho.html', context)

    def post(self, request):

        if request.method == 'POST':

            kho = Khohang.objects.get(pk=request.POST.get('kho'))
            code = request.POST.get('code')
            nhacungcap = Nhacungcap.objects.get(pk=request.POST.get('nhacungcap'))
            thoigiantao = request.POST.get('thoigiantao')
            thoigiannhanhang = request.POST.get('thoigiannhanhang')
            nhanvien = Nhanvien.objects.get(username=request.user)
            ghichu = request.POST.get('ghichu')
            tinhtrang = False
            tuchoi = False
            if request.POST.get('courses'):
                tenhang_d1 = Hanghoa.objects.get(pk=request.POST.get('courses'))
                tenhang_1 = tenhang_d1.tenhanghoa
            else:
                tenhang_1 = None
            if request.POST.get('courses2'):
                tenhang_d2 = Hanghoa.objects.get(pk=request.POST.get('courses2'))
                tenhang_2 = tenhang_d2.tenhanghoa
            else:
                tenhang_2 = None
            if request.POST.get('courses3'):
                tenhang_d3 = Hanghoa.objects.get(pk=request.POST.get('courses3'))
                tenhang_3 = tenhang_d3.tenhanghoa
            else:
                tenhang_3 = None
            if request.POST.get('courses4'):
                tenhang_d4 = Hanghoa.objects.get(pk=request.POST.get('courses4'))
                tenhang_4 = tenhang_d4.tenhanghoa
            else:
                tenhang_4 = None

            noidung = {

                'hang_1': request.POST.get('courses'),
                'tenhang_1': tenhang_1,
                'soluong_1': request.POST.get('soluong1'),
                'dongia_1': request.POST.get('dongia1'),
                'hang_2': request.POST.get('courses2'),
                'tenhang_2': tenhang_2,
                'soluong_2': request.POST.get('soluong2'),
                'dongia_2': request.POST.get('dongia2'),
                'hang_3': request.POST.get('courses3'),
                'tenhang_3': tenhang_3,
                'soluong_3': request.POST.get('soluong3'),
                'dongia_3': request.POST.get('dongia3'),
                'hang_4': request.POST.get('courses4'),
                'tenhang_4': tenhang_4,
                'soluong_4': request.POST.get('soluong4'),
                'dongia_4': request.POST.get('dongia14')
            }

            Phieunhaphang.objects.create(code=code, nhacungcap=nhacungcap, noidung=noidung
                                         , username=request.user, nhanvien=nhanvien, kho=kho, tinhtrang=tinhtrang,
                                         thoigiantao=thoigiantao
                                         , thoigiannhanhang=thoigiannhanhang, ghichu=ghichu, tuchoi=tuchoi)

            return redirect('nhap-hang')


class Viewphieunhap(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request, code_id):
        phieunhaphang = Phieunhaphang.objects.get(pk=code_id)
        nd = phieunhaphang.noidung
        hangsx = Hangsx.objects.all()
        hanghoa = Hanghoa.objects.all()
        khohang = Khohang.objects.all()
        thukho = Thukho_Khohang.objects.all()
        nhanvien = Nhanvien.objects.get(tennv=phieunhaphang.nhanvien)
        nhancungcap = Nhacungcap.objects.all()
        formedit = Editnhaphang(instance=phieunhaphang)

        context = {
            'phieunhaphang': phieunhaphang,
            'noidung': nd,
            'hangsx': hangsx,
            'hanghoa': hanghoa,
            'khohang': khohang,
            'thukho': thukho,
            'nhanvien': nhanvien,
            'nhancungcap': nhancungcap,
            'form':formedit,

        }
        return render(request, 'viewphieunhaphang.html', context)


    def post(self,request,code_id):


        if request.POST.get('courses'):
            tenhang_d1 = Hanghoa.objects.get(pk=request.POST.get('courses'))
            tenhang_1 = tenhang_d1.tenhanghoa
        else:
            tenhang_1 = None
        if request.POST.get('courses2'):
            tenhang_d2 = Hanghoa.objects.get(pk=request.POST.get('courses2'))
            tenhang_2 = tenhang_d2.tenhanghoa
        else:
            tenhang_2 = None
        if request.POST.get('courses3'):
            tenhang_d3 = Hanghoa.objects.get(pk=request.POST.get('courses3'))
            tenhang_3 = tenhang_d3.tenhanghoa
        else:
            tenhang_3 = None
        if request.POST.get('courses4'):
            tenhang_d4 = Hanghoa.objects.get(pk=request.POST.get('courses4'))
            tenhang_4 = tenhang_d4.tenhanghoa
        else:
            tenhang_4 = None
        noidung = {

            'hang_1': request.POST.get('courses'),
            'tenhang_1': tenhang_1,
            'soluong_1': request.POST.get('soluong1'),
            'dongia_1': request.POST.get('dongia1'),
            'hang_2': request.POST.get('courses2'),
            'tenhang_2': tenhang_2,
            'soluong_2': request.POST.get('soluong2'),
            'dongia_2': request.POST.get('dongia2'),
            'hang_3': request.POST.get('courses3'),
            'tenhang_3': tenhang_3,
            'soluong_3': request.POST.get('soluong3'),
            'dongia_3': request.POST.get('dongia3'),
            'hang_4': request.POST.get('courses4'),
            'tenhang_4': tenhang_4,
            'soluong_4': request.POST.get('soluong4'),
            'dongia_4': request.POST.get('dongia14')
        }

        return redirect('nhap-hang')


class Xuathang(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        return render(request, 'xuathang.html')


class Dieuchuyenkho(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        return render(request, 'dieuchuyenkho.html')


class Tonkho(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        return render(request, 'tonkho.html')


class load_courses(View):

    def get(self, request):
        programming_id = request.GET.get('programming')
        programming_id2 = request.GET.get('programming2')
        programming_id3 = request.GET.get('programming3')
        programming_id4 = request.GET.get('programming4')
        nhanvien_id = request.GET.get('nhanvien_id')

        nhanvien = Nhanvien.objects.filter(id=nhanvien_id)

        courses = Hanghoa.objects.filter(hangsx=programming_id).order_by('tenhanghoa')
        courses2 = Hanghoa.objects.filter(hangsx=programming_id2).order_by('tenhanghoa')
        courses3 = Hanghoa.objects.filter(hangsx=programming_id3).order_by('tenhanghoa')
        courses4 = Hanghoa.objects.filter(hangsx=programming_id4).order_by('tenhanghoa')

        context = {
            'courses': courses,
            'courses2': courses2,
            'nhanvien': nhanvien,
            'courses3': courses3,
            'courses4': courses4,

        }
        return render(request, 'load_hanghoa.html', context)


class Quanlynhaphang(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        phieuhang = Phieunhaphang.objects.all()
        demph_duyet = 0
        demph_chua_duyet_gap=0
        demph_chua_duyet=0
        i = 0
        j = 0
        k = -1
        for item in phieuhang:
            if item.tinhtrang==True:
                i+=1
            if item.tinhtrang==False:
                j+=1
            if item.tinhtrang==False and item.tuchoi==False :
                if 'GẤP' in item.ghichu:
                    k+=1
            demph_duyet =i
            demph_chua_duyet = j
            demph_chua_duyet_gap = k

        context={
            'demph_duyet':demph_duyet,
            'demph_chua_duyet':demph_chua_duyet,
            'demph_chua_duyet_gap':demph_chua_duyet_gap
        }
        return render(request, 'quanly.html',context)

    def post(self, request):
        pass


class Nhaphangchuaduyet(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        hanghoa = Hanghoa.objects.all()
        khohang = Khohang.objects.all()
        pnh_nonactive = Phieunhaphang.objects.filter(tinhtrang=False)

        context = {
            'hanghoa': hanghoa,
            'khohang': khohang,
            'pnh_nonactive': pnh_nonactive,

        }
        return render(request, 'nhaphangchuaduyet.html', context)


class Nhaphangchuaduyetgap(LoginRequiredMixin, View):
    login_url = 'login/'
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        hanghoa = Hanghoa.objects.all()
        khohang = Khohang.objects.all()
        pnh_nonactive = Phieunhaphang.objects.filter(tinhtrang=False, ghichu='GẤP')

        context = {
            'hanghoa': hanghoa,
            'khohang': khohang,
            'pnh_nonactive': pnh_nonactive,

        }
        return render(request, 'nhaphangchuaduyetgap.html', context)


class Duyetnhaphang(LoginRequiredMixin, View):
    def get(self, request, code_id):
        user = request.user


        if user.username == 'thangnguyen':
            nhaphang = Phieunhaphang.objects.get(pk=code_id)
            form = Nhaphangchuaduyetgaps(instance=nhaphang)
            context = {
                'phieunhaphang': nhaphang,
                'form':form
                }
            return render(request, 'duyetnhaphang.html', context)
        else:
            return HttpResponse("Ban Khong Phai Nguyen Minh Thang")

    def post(self, request, code_id):
        print(request.POST)
        user = request.user
        if user.username == 'thangnguyen':
            pl = Phieunhaphang.objects.get(pk=code_id)
            form = Nhaphangchuaduyetgaps(request.POST,instance=pl)
            if form.is_valid():
                form.save()
        return redirect('nhaphangchuaduyetgap')
