from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User


class Phongban(models.Model):
    tenpb = models.CharField(default='',unique=True,max_length=255,verbose_name='Tên Phòng Ban')
    ngaythanhlap = models.DateTimeField(verbose_name='Năm thành lập',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = "PHÒNG BAN"
        verbose_name_plural = 'PHÒNG BAN'

    def __str__(self):
        return self.tenpb

class Nhanvien(models.Model):
    manv = models.CharField(default='',unique=True,max_length=255,verbose_name='Mã Nhân Viên')
    username = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Tài Khoản Nhân Viên')
    tennv = models.CharField(default='', max_length=255, verbose_name='Họ Tên Nhân Viên')
    gioitinh = models.BooleanField(default='',verbose_name='Check - Nếu là nam')
    ngaysinh =models.DateField(verbose_name='Ngày Sinh')
    diachi = models.CharField(default='', max_length=255, verbose_name='Địa chỉ thường trú')
    quequan =models.CharField(default='', max_length=255, verbose_name='Quê Quán')
    cmnd = models.CharField(default='', max_length=12, verbose_name='CCID')
    cmnd_1 =models.ImageField(default='',null=True, blank=True,upload_to='img/', verbose_name='Ảnh mặt trước CCID')
    cmnd_2 =models.ImageField(default='',null=True, blank=True, upload_to='img/', verbose_name='Ảnh mặt sau CCID')
    avatar = models.ImageField(default='',null=True, blank=True, upload_to='img/', verbose_name='Ảnh chân dung')
    sdt = models.CharField(default='', unique=True, max_length=255, verbose_name='Số Điện Thoại')
    line= models.CharField(default='', max_length=255, verbose_name='Line nội bộ')
    email =models.CharField(default='',unique=True, null=True,blank=True ,max_length=255, verbose_name='Email')
    phongban = models.ForeignKey(Phongban,default='',null=True,blank=True,on_delete=models.CASCADE)
    tinhtrangcongviec = models.BooleanField(default='1',verbose_name='Check --- (nếu nhân viên chính thức) ')
    chuky1 =models.FileField(blank=True,null=True,verbose_name='Upload chữ ký 1 ')
    chuky2 = models.FileField(blank=True, null=True, verbose_name='Upload chữ ký 2 ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "NHÂN VIÊN"
        verbose_name_plural = 'NHÂN VIÊN'


    def __str__(self):
        return self.tennv
class Chucvu_Congviec(models.Model):
    nhanvien = models.ForeignKey(Nhanvien ,on_delete=models.CASCADE,verbose_name='Nhân Viên')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name='Phòng ban')
    tencongviec = models.CharField(default='', unique=True, max_length=255, verbose_name='Tên Công việc+ Chúc Vụ')
    motacongviec = models.TextField(verbose_name='Mô tả công việc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "NHÂN VIÊN CHỨC VỤ"
        verbose_name_plural = 'NHÂN VIÊN CHỨC VỤ'

    def __int__(self):
        return self.nhanvien

class Baohiemyte(models.Model):
    nhanvien =models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhyt = models.CharField(default='', unique=True, max_length=255, verbose_name='Mã Số BHXH')
    ngaythamgia = models.DateField(verbose_name='Ngày tham gia')
    noidangky = models.CharField(default='', max_length=255, verbose_name='Nơi đăng ký BHYT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "BẢO HIỂM Y TẾ"
        verbose_name_plural = 'BẢO HIỂM Y TẾ'
    def __str__(self):
        return self.masobhyt

class Baohiemxahoi(models.Model):
    nhanvien = models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhxh = models.CharField(unique=True,max_length=255,verbose_name='Mã Số BHXH')
    ngaythamgia =  models.DateField(verbose_name='Ngày tham gia')
    noidangky = models.CharField(default='', max_length=255, verbose_name='Địa chỉ đăng ký')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "BẢO HIỂM XÃ HỘI"
        verbose_name_plural = 'BẢO HIỂM XÃ HỘI'
    def __str__(self):
        return self.masobhxh

class Quatrinhdongbhxh(models.Model):
    tennhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Nhân Viên Đóng BHXH')
    thoigiandong = models.DateTimeField(verbose_name='Ngày-Tháng-Năm Đóng')
    sotiendong   = models.CharField(default='',max_length=255,verbose_name='Số Tiền Đóng BHXH')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "QUÁ TRÌNH ĐÓNG BẢO HIỂM XÃ HỘI"
        verbose_name_plural = "QUÁ TRÌNH ĐÓNG BẢO HIỂM XÃ HỘI"
    def __int__(self):
        return self.tennhanvien


class Hosonhanvien(models.Model):
    nhanvien = models.OneToOneField(Nhanvien, on_delete=models.CASCADE,verbose_name='Họ Tên Nhân Viên')
    masobh = models.CharField(unique=True,max_length=255,verbose_name='Mã Số HDLD ')
    ngaythuviec =  models.DateField(verbose_name='Ngày thử việc')
    ngaychinhthuc = models.DateField(verbose_name='Ngày làm chính thức')
    chuyenmon = models.CharField(default='', max_length=255, verbose_name='Chuyên ngành')
    vanhoa = models.CharField(default='', max_length=255, verbose_name='Trình độ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "HỒ SƠ NHÂN VIÊN"
        verbose_name_plural = 'HỒ SƠ NHÂN VIÊN'
    def __int__(self):
        return self.nhanvien


class Loaihopdong(models.Model):
    maloaihd = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    tenhd = models.CharField(default='', max_length=255,blank=True,null=True, verbose_name='Mô Tả Hợp Đồng')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "LOẠI HỢP ĐỒNG"
        verbose_name_plural = 'LOẠI HỢP ĐỒNG'

    def __str__(self):
        return self.maloaihd

class Quanlyhopdongkinhdoanh(models.Model):
    masohopdong = models.CharField(default='',unique=True, max_length=255, verbose_name='Mã Số Hợp Đồng')
    tenhopdong  = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    khachhang = models.CharField(default='', max_length=255, verbose_name='Tên Khách Hàng')
    ngaytrinhky = models.DateField(default='', max_length=255, verbose_name='Ngày Trình Ký Hợp Đồng')
    filehopdong = models.FileField()
    loaihd  = models.ForeignKey(Loaihopdong,default='',on_delete=models.CASCADE, verbose_name='Loại Hợp Đồng')
    nhanvien = models.ForeignKey(Nhanvien,default='',on_delete=models.CASCADE, verbose_name='Nhân Viên phụ trách')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "QUẢN LÝ HỢP ĐỒNG CÔNG TY"
        verbose_name_plural = 'QUẢN LÝ HỢP ĐỒNG CÔNG TY'

    def __int__(self):
        return self.nhanvien


class Phieuluong_upload(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    thang = models.CharField(default='',null=True, blank=True, max_length=255)
    nam = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaylamthucte = models.CharField(default='', null=True, blank=True,max_length=255)
    congchuan = models.CharField(default='', null=True, blank=True,max_length=255)
    congthembot = models.CharField(default='',null=True, blank=True, max_length=255)
    luongcoban = models.CharField(default='',null=True, blank=True, max_length=255)
    phucap = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoai = models.CharField(default='', null=True, blank=True,max_length=255)
    tienxang = models.CharField(default='', null=True, blank=True,max_length=255)
    tiencom = models.CharField(default='',null=True, blank=True, max_length=255)
    luongtrachnhiem = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoaihotro = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaynghikhongpep = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongnghikhongphep = models.CharField(default='', null=True, blank=True,max_length=255)
    hotrobaohiemtrongluong = models.CharField(default='', null=True, blank=True,max_length=255)
    luoncnx2 = models.CharField(default='', null=True, blank=True,max_length=255)
    tongthunhap = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienunggiuathang = models.CharField(default='',null=True, blank=True, max_length=255)
    trutienmatunggiuathang = models.CharField(default='', null=True, blank=True,max_length=255)
    trutiendienthoaicongtytraho = models.CharField(default='',null=True, blank=True, max_length=255)
    trunotrongthang = models.CharField(default='',null=True, blank=True, max_length=255)
    trubaohiem = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienphat = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongluyke = models.CharField(default='', null=True, blank=True,max_length=255)
    tienluongthuclanhcuoithang = models.CharField(default='',null=True, blank=True, max_length=255)
    nothangtruoc = models.CharField(default='', null=True, blank=True,max_length=255)
    muonnothangnay = models.CharField(default='', null=True, blank=True,max_length=255)
    trunotrongluong = models.CharField(default='',null=True, blank=True, max_length=255)
    thunotienmat = models.CharField(default='', null=True, blank=True, max_length=255)
    noconluanchuyensangthangsau = models.CharField(default='',null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = " UPLOAD PHIẾU LƯƠNG"
        verbose_name_plural = 'UPLOAD PHIẾU LƯƠNG'

    def __int__(self):
        return self.nhanvien
