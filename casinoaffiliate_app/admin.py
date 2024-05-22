from django.contrib import admin
from casinoaffiliate_app.models import Casino, GameTransaction, Bonus, AdminReview, GameAccount, GameDeposit, GameWithdrawal

class CasinoAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort']

class GameAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']

class GameTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'created_at']

admin.site.register(Casino, CasinoAdmin)
admin.site.register(Bonus)
admin.site.register(AdminReview)
admin.site.register(GameAccount,GameAccountAdmin)
#admin.site.register(GameDeposit)
admin.site.register(GameWithdrawal)
admin.site.register(GameTransaction, GameTransactionAdmin)
