from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'dong_b'
    site_title = 'dong_b管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')
