from django.contrib import admin

from .models import Vendor,Assets,AssetTrans,Delivery


# class QuestionAdmin(admin.ModelAdmin):
#     fields=['pub_date', 'question_text']

class TransAdmin(admin.ModelAdmin):
    list_display = ('delivery','assetId','qty', 'transDate', 'shipped', 'received')


admin.site.register(Vendor)

admin.site.register(Assets)
admin.site.register(Delivery)

admin.site.register(AssetTrans, TransAdmin)

