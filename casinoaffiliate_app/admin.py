from django.contrib import admin
from casinoaffiliate_app.models import Casino, Bonus, AdminReview, GameAccount, GameDepositt, GameWithdrawall

class CasinoAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort']

admin.site.register(Casino, CasinoAdmin)
admin.site.register(Bonus)
admin.site.register(AdminReview)
admin.site.register(GameAccount)
admin.site.register(GameDepositt)
admin.site.register(GameWithdrawall)
