"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from qlns.views import (Dsnhanvien,Profile,Logout,Phieuluonguser,Phieuluongcanhan,
                        Index,Login,Giaoviec,Nhanvientotal,Viewnhanvien,Changenhanvien,
                        Deletenhanvien,Delete_checkbox,Phieuluongupload,Getnhanvien)
from khovan.views import *
from django.conf import settings

from django.conf.urls.static import static

admin.site.index_title="Quản Trị Hệ Thống"
urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('', Index.as_view(),name='index'),
    path('login/', Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('giao-viec/', Giaoviec.as_view(),name='giaoviec'),
    path('nhanvien/', Nhanvientotal.as_view(), name='nhanvien'),
    path('get-nhan-vien/', Getnhanvien.as_view(),name='getnhanvien'),
    path('profile/',Profile.as_view(),name='profile'),
    path('dsnhanvien/',Dsnhanvien.as_view(),name='dsnhanvien'),
    path('viewnhanvien/', Viewnhanvien.as_view(), name='viewnhanvien'),
    path('deletenhanvien/',Delete_checkbox.as_view(), name='delete-nhanvien'),
    path('phieu-luong-upload/',Phieuluongupload.as_view(), name='phieuluongupload'),
    path('nhanvien/delete/<int:nhanvien_id>',Deletenhanvien.as_view(),name='deletenhanvien'),
    path('nhan-vien/xem-nhan-vien/<int:nhanvien_id>', Changenhanvien.as_view(), name='xemnhanvien'),
    path('phieu-luong/nhan-vien/<int:nhanvien_id>', Phieuluongcanhan.as_view(), name='xemphieuluong'),
    path('phieu-luong-user', Phieuluonguser.as_view(), name='xemphieuluonguser'),
    path('nhap-hang/',Nhaphangs.as_view(),name="nhap-hang"),
    path('nhap-hang/<int:code_id>',Viewphieunhap.as_view(),name='view-nhap-hang'),
    path('phieu-nhap-kho/',Phieunhapkho.as_view(),name="phieu-nhap-kho"),
    path('load-courses/', load_courses.as_view(), name='ajax_load_courses'),
    path('quan-ly-nhap-hang',Quanlynhaphang.as_view(),name="quan-ly-nhap-hang"),
    path('nhap-hang-chua-duyet',Nhaphangchuaduyet.as_view(),name='nhaphangchuaduyet'),
    path('nhap-hang-chua-duyet-gap',Nhaphangchuaduyetgap.as_view(),name='nhaphangchuaduyetgap'),
    path('duyet-nhap-hang/<int:code_id>',Duyetnhaphang.as_view(),name='duyetnhaphang'),
    path('xuat-hang/',Xuathang.as_view(),name="xuat-hang"),
    path('ton-kho/',Tonkho.as_view(),name="ton-kho"),
    path('kho-van/thu-kho',Thukho.as_view(),name="thu-kho"),
    path('dieu-chuyen-kho/',Dieuchuyenkho.as_view(),name="dieu-chuyen-kho"),
              ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
