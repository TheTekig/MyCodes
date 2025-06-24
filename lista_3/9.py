anacleto = 1.50
agrow = 0.02
felisberto = 1.10
fgrow = 0.03
years = 0

while anacleto >= felisberto:

    years = years + 1
    anacleto = anacleto + agrow
    felisberto = felisberto + fgrow

print("Anacleto apos %d anos tera %.2fcm e felisberto %.2fcm" %(years,anacleto,felisberto))