from django.contrib import admin
from Api.models import User,Team,LeagueType,League,Prediction,Unit,CompletedText,PredictionDetail,PurchasedPrediction,tempUser,Profile,Credit,PurchasedCredit,UserCredit

class PredictionAdmin(admin.ModelAdmin):
     
     fieldsets = [
        (None,               {'fields': ['leagueType','league','homeTeam','awayTeam','tipDetail','isPushNotifSend','isCompleted'
                              , 'completedText','DateTimeCreated','DateTimeCompleted']}),
        ('isPredictionVerified', {'fields': ['verified','covered','pending']}),
    ]
     list_display = ('id','leagueType','homeTeam','awayTeam','isPushNotifSend','isCompleted','isPredictionVerified')
     list_filter =  ['isCompleted']

class UserCreditAdmin(admin.ModelAdmin):
     list_display = ('id','user','credit')

class PurchasedCreditAdmin(admin.ModelAdmin):
      list_display = ('id','userID','dateTime','credit','creditID')

class LeagueTypeAdmin(admin.ModelAdmin):
     list_display = ('name','countryFlagUrl')

class PredictionDetailAdmin(admin.ModelAdmin):
     list_display = ('id','name','message')

class PurchasedPredictionAdmin(admin.ModelAdmin):
     list_display = ('id','userID','predictionID')

#admin.site.register(User,UserAdmin)
admin.site.register(Team)
admin.site.register(UserCredit,UserCreditAdmin)
admin.site.register(LeagueType,LeagueTypeAdmin)
admin.site.register(League)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(Unit)
admin.site.register(PurchasedCredit,PurchasedCreditAdmin)
admin.site.register(Credit)
admin.site.register(CompletedText)
admin.site.register(PredictionDetail,PredictionDetailAdmin)
admin.site.register(PurchasedPrediction,PurchasedPredictionAdmin)

#admin.site.register(tempUser)
#admin.site.register(Profile)



# Register your models here.

