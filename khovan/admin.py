from django.contrib import admin
from .models import (Gas,Loaimay,Congsuat,Hemay,
                     Nganhhang,Hangsx,Hanghoa,Khohang,Thukho_Khohang,
                     Ton_kho,Nhaphang,Xuathang,Phieunhaphang,Nhacungcap)
from khovan.resources import HanghoaResource
from khovan.models import Hanghoa,Hangsx,Nganhhang
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

admin.site.register(Gas,ImportExportActionModelAdmin)
admin.site.register(Loaimay,ImportExportActionModelAdmin)
admin.site.register(Congsuat,ImportExportActionModelAdmin)
admin.site.register(Nhacungcap,ImportExportActionModelAdmin)
class HemayAdmins(admin.ModelAdmin):
    list_display = ('id','tenhemay','view_hanghoa')
    search_fields = ('tenhemay',)
    list_per_page = 10
    def view_hanghoa(self,obj):
        count = obj.hanghoa_set.count()
        url = (
                reverse("admin:khovan_hanghoa_changelist")
                + "?"
                + urlencode({"nganhhang__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Model</a>', url, count)

    view_hanghoa.short_description = "Số Model"
admin.site.register(Hemay,HemayAdmins)

class HangsxAdmins(ImportExportActionModelAdmin):
    list_display = ('id','tenhangsx','view_hanghoa')
    search_fields = ('tenhangsx',)


    def view_hanghoa(self,obj):
        count = obj.hanghoa_set.count()
        url = (
                reverse("admin:khovan_hanghoa_changelist")
                + "?"
                + urlencode({"hangsx__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}  Model</a>', url, count)

    view_hanghoa.short_description = "Số Model"

admin.site.register(Hangsx,HangsxAdmins)

class HanghoaAdmins(ImportExportActionModelAdmin):
    list_display = ('code','tenhanghoa','hangsx', 'congsuat', 'gas', 'giavon')
    search_fields = ('tenhanghoa',)
    list_filter = ('hangsx','congsuat',)
    list_per_page = 10
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    resource_class = HanghoaResource
admin.site.register(Hanghoa,HanghoaAdmins)


class NganhhangAdmins(admin.ModelAdmin):
    list_display = ('id','tennghanhhang','view_hanghoa')
    search_fields = ('tennghanhhang',)
    list_per_page = 10
    def view_hanghoa(self,obj):
        count = obj.hanghoa_set.count()
        url = (
                reverse("admin:khovan_hanghoa_changelist")
                + "?"
                + urlencode({"nganhhang__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Model</a>', url, count)

    view_hanghoa.short_description = "Số Model"
admin.site.register(Nganhhang,NganhhangAdmins)


class KhohangAdmins(admin.ModelAdmin):

    list_display = ('id','tenkho',)
    search_fields = ('tenkho',)
    list_per_page = 10

admin.site.register(Khohang,KhohangAdmins)


class Thukho_KhohangAdmins(admin.ModelAdmin):
    list_display = ('id', 'nhanvien','kho')
    search_fields = ('nhanvien',)
    list_per_page = 10


admin.site.register(Thukho_Khohang, Thukho_KhohangAdmins)

class XuathangAdmins(admin.ModelAdmin):
    list_display = ('id','hanghoa','soluong','kho','tinhtrang',)
    search_fields = ('hanghoa',)
    list_editable = ('hanghoa','soluong','kho','tinhtrang')
    list_per_page = 10
    actions = ('active','chuyển_tình_trạng_chưa_xuất_kho')
    def active(self,request,queryset):
        queryset.update(tinhtrang = True)
    active.short_description = "Xác Nhận Xuất Hàng"
    def nonactive(self,request,queryset):
        queryset.update(tinhtrang = False)

admin.site.register(Xuathang, XuathangAdmins)


class NhaphangAdmins(admin.ModelAdmin):
    list_display = ( 'id','hanghoa','soluong',)
    search_fields = ('hanghoa',)
    list_per_page = 10


admin.site.register(Nhaphang, NhaphangAdmins)

class TonkhoAdmins(admin.ModelAdmin):
    list_display = ('id',"hanghoa",'soluongnhap','soluongxuat','kho')
    list_per_page = 10



admin.site.register(Ton_kho, TonkhoAdmins)
admin.site.register(Phieunhaphang,ImportExportActionModelAdmin)

