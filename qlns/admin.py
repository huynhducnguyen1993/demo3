from django.contrib import admin
from .models import (User,Quatrinhdongbhxh,Phieuluong_upload,
                     Nhanvien,Phongban,Chucvu_Congviec,Loaihopdong,
                     Phieuluong_upload,Quanlyhopdongkinhdoanh,Baohiemyte,Baohiemxahoi,Hosonhanvien)
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from qlns.models import Nhanvien
from qlns.resources import NhanvienResource
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
# Register your models here.



admin.site.site_header="Đông Sapa"

class PhieuluongAdmins(ImportExportActionModelAdmin):
    list_display = ('id','nhanvien', 'thang', 'nam', 'tongthunhap')
    search_fields = ('nhanvien',)
    list_filter = ('thang','nam')
    list_per_page = 10
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)


admin.site.register(Phieuluong_upload, PhieuluongAdmins)
admin.site.register(Loaihopdong)
class NhanvienAdmins(ImportExportActionModelAdmin):
    list_display = ('id','manv', 'tennv', 'username', 'cmnd_1')
    search_fields = ('tennv',)
    list_filter = ('phongban',)
    list_per_page = 10
    resource_class = NhanvienResource

admin.site.register(Nhanvien, NhanvienAdmins)

class PhongbanAdmin(ImportExportActionModelAdmin):
    list_display = ('id','tenpb', 'ngaythanhlap','view_nhanvien')
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    def view_nhanvien(self,obj):
        count = obj.nhanvien_set.count()
        url = (
                reverse("admin:qlns_nhanvien_changelist")
                + "?"
                + urlencode({"phongban__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} nhân Viên</a>', url, count)

    view_nhanvien.short_description = "Số Nhân Viên"
    # tính tổng nhân viên trong 1 phòngs

    def before_save_instance(self, instance):
        format_str = '%d/%m/%y'  # the format in which dates are stored in CSV file
        instance.created_at = datetime.strptime(instance.created_at, format_str)
        instance.updated_at = datetime.strptime(instance.updated_at, format_str)
        return instance



admin.site.register(Phongban, PhongbanAdmin)


# class NhanvienAdmin(admin.ModelAdmin):
#     list_display = ('manv', 'tennv', 'username', 'cmnd_1')
#     list_filter = ('phongban',)
#     search_fields = ('tennv',)
#     list_per_page = 10
#
# admin.site.register(Nhanvien, NhanvienAdmin)




class NhanvienChucvuAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'phongban','tencongviec')


admin.site.register(Chucvu_Congviec, NhanvienChucvuAdmin)

class BaohiemxahoiAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'masobhxh','ngaythamgia','noidangky')


admin.site.register(Baohiemxahoi, BaohiemxahoiAdmin)


class BaohiemytAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'masobhyt','ngaythamgia','noidangky')


admin.site.register(Baohiemyte, BaohiemytAdmin)

class HosoAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'masobh','ngaythuviec','ngaychinhthuc')


admin.site.register(Hosonhanvien, HosoAdmin)

class HosokinhdoanhAdmin(admin.ModelAdmin):
    list_display = ('masohopdong', 'tenhopdong','ngaytrinhky','filehopdong','nhanvien','created_at','updated_at')


admin.site.register(Quanlyhopdongkinhdoanh, HosokinhdoanhAdmin)

class QtdbhxhAdmin(ImportExportActionModelAdmin):
    list_display = ('tennhanvien','thoigiandong')
    list_filter = ('tennhanvien','thoigiandong',)
    list_per_page = 10
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
admin.site.register(Quatrinhdongbhxh,QtdbhxhAdmin)

