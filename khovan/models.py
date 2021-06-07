from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from qlns.models import Nhanvien
# Create your models here.


class Gas(models.Model):
    tengas = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name='Loại Gas')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "LOẠI GAS"
        verbose_name_plural = 'LOẠI GAS'

    def __str__(self):
        return self.tengas
class Loaimay(models.Model):
    tenloai = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name='Loại Máy')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "LOẠI MÁY "
        verbose_name_plural = 'LOẠI MÁY '

    def __str__(self):
        return self.tenloai

class Congsuat(models.Model):
    tencongsuat = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name=' Công suất ')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "CÔNG SUẤT "
        verbose_name_plural = 'CÔNG SUẤT '

    def __str__(self):
        return self.tencongsuat

class Hemay(models.Model):
    tenhemay = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name=' Hệ Máy ')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "HỆ MÁY"
        verbose_name_plural = 'HỆ MÁY'

    def __str__(self):
        return self.tenhemay

class Nganhhang(models.Model):
    tennghanhhang = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name='Tên Nghành Hàng ')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "NGÀNH HÀNG "
        verbose_name_plural = 'NGÀNH HÀNG '

    def __str__(self):
        return self.tennghanhhang
class Hangsx(models.Model):
    tenhangsx = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name='Tên Hãng ')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "HÃNG SX "
        verbose_name_plural = 'HÃNG SX '

    def __str__(self):
        return self.tenhangsx


class Hanghoa(models.Model):
    code = models.IntegerField(default=0,unique=True)
    tenhanghoa = models.CharField(default='',max_length=100,blank=False,null=False,verbose_name='Tên Hàng Hoá (Dàn Lạnh/ Dàn Nóng.)')
    hangsx = models.ForeignKey(Hangsx,on_delete=models.CASCADE,verbose_name='Hãng Sản Xuất')
    nganhhang = models.ForeignKey(Nganhhang,on_delete=models.CASCADE,verbose_name='Danh Mục')
    hemay = models.ForeignKey(Hemay,on_delete=models.CASCADE,verbose_name='Hệ Máy ')
    congsuat = models.ForeignKey(Congsuat,on_delete=models.CASCADE,verbose_name='Công Suất')
    loaimay =  models.ForeignKey(Loaimay,on_delete=models.CASCADE,verbose_name='Loại Máy ')
    gas = models.ForeignKey(Gas,on_delete=models.CASCADE,verbose_name='Loại Gas ')
    giavon = models.IntegerField(default='0',blank=True,null=True,verbose_name='Giá Vốn ')
    mota = models.CharField(max_length=500,blank=True,null=True,verbose_name='Mô tả (có thể bỏ trống)')
    class Meta:
        verbose_name = "HÀNG HOÁ "
        verbose_name_plural = 'HÀNG HOÁ'

    def __str__(self):
        return self.tenhanghoa

class Khohang(models.Model):
    tenkho = models.CharField(max_length=200,blank=False,null=False,verbose_name='Tên Kho')
    diachi = models.CharField(max_length=500,blank=True,null=True,verbose_name='Địa Chỉ')
    class Meta:
        verbose_name = "KHO HÀNG "
        verbose_name_plural = 'KHO HÀNG'

    def __str__(self):
        return self.tenkho

class Thukho_Khohang(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    kho = models.ForeignKey(Khohang,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "THỦ KHO"
        verbose_name_plural = 'THỦ KHO'

    def __str__(self):
        return self.nhanvien

class Nhaphang(models.Model):
    hanghoa = models.ForeignKey(Hanghoa, on_delete=models.CASCADE,verbose_name='Tên Hàng Hoá')
    soluong = models.IntegerField(default=0,blank=True,verbose_name='Số Lượng')
    kho = models.ForeignKey(Khohang,on_delete=models.CASCADE)
    tinhtrang = models.BooleanField(verbose_name='Tình Trạng -( Check Nếu Hàng Đã Thực Nhập )')

    class Meta:
        verbose_name = "NHẬP HÀNG "
        verbose_name_plural = 'NHẬP HÀNG'

    def __str__(self):
        return self.hanghoa


class Nhacungcap(models.Model):
    tennhacungcap =  models.CharField(max_length=200,blank=False,null=False,verbose_name='Tên Nhà Cung Cấp')
    diachinhacungcap =  models.CharField(max_length=200,blank=False,null=False,verbose_name='Địa chỉ nhà cung cấp')
    diachikhonhacungcap = models.CharField(max_length=200,blank=False,null=False,verbose_name='Địa chỉ nhà cung cấp')
    nhanvienquanly = models.ForeignKey(Nhanvien ,on_delete=models.CASCADE, verbose_name='Tên Nhân Viên Quản Lý')
    hanmuccongno = models.FloatField(default=0, blank=True,null=True,verbose_name='Hạn mức ')

    def __str__(self):
        return self.tennhacungcap

    class Meta:
        verbose_name = "NHÀ CUNG CẤP "
        verbose_name_plural = 'NHÀ CUNG CẤP'


class Phieunhaphang(models.Model):

    code  =  models.CharField(max_length=200,blank=False,null=False,verbose_name='Barcode',unique=True)
    nhacungcap  =  models.ForeignKey(Nhacungcap, on_delete = models.CASCADE, verbose_name='Nhà cung cấp' )
    noidung = models.JSONField(blank=False,null = False,verbose_name='Nội Dung ')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Tài Khoản')
    nhanvien =  models.CharField(max_length=200,blank=True,null=True,verbose_name='Tên Kinh doanh(không  điền trường này)')
    kho = models.ForeignKey(Khohang, on_delete=models.CASCADE, verbose_name='Kho')
    tinhtrang = models.BooleanField(verbose_name='Duyệt')
    tuchoi = models.BooleanField(verbose_name='Từ Chối')
    thoigiantao = models.DateField()
    thoigiannhanhang = models.DateField()
    ghichu = models.CharField(default=".",max_length=200,blank=False,null=False,verbose_name='Ghi Chú  ')
    phanhoi =  models.CharField(default=".",max_length=200,blank=False,null=False,verbose_name='Phản Hồi  ')

    class Meta:
        verbose_name = "PHIẾU NHẬP XUẤT HÀNG "
        verbose_name_plural = 'PHIẾU NHẬP XUẤT HÀNG'

    def __str__(self):
        return self.code

class Xuathang(models.Model):

    hanghoa = models.ForeignKey(Hanghoa, on_delete=models.CASCADE, verbose_name='Tên Hàng Hoá')
    soluong = models.IntegerField(default=0, verbose_name='Số Lượng')
    kho = models.ForeignKey(Khohang, on_delete=models.CASCADE, verbose_name='Tên Kho')

    tinhtrang = models.BooleanField(verbose_name='Tình Trạng -(Check Nếu Hàng Đã Thực Xuất)')

    class Meta:
        verbose_name = "XUẤT HÀNG "
        verbose_name_plural = 'XUẤT HÀNG'

    def __str__(self):
        return self.hanghoa



class Ton_kho(models.Model):
    hanghoa = models.ForeignKey(Hanghoa, on_delete=models.CASCADE, verbose_name='Tên Hàng Hoá')
    soluongnhap = models.IntegerField(default=0, verbose_name='Số Lượng Nhập')
    soluongxuat = models.IntegerField(default=0, verbose_name='Số Lượng Xuất')
    kho = models.ForeignKey(Khohang, on_delete=models.CASCADE, verbose_name='Tên Kho')

    def __str__(self):
        return self.hanghoa

    class Meta:
        verbose_name = "TỒN KHO "
        verbose_name_plural = 'TỒN KHO'
