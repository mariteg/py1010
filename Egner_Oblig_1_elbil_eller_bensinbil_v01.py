# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:34:05 2024

@author: mareg
"""
# Jeg skal regne ut prisforskjellen per år for bensinbil og elbil
# Min familie kjører ca 12000 km per år
# km/år likt for begge biler
km = 12000

#Forsikring i kr per år
ElFors = 5000

BensinFors = 7500
#Trafikkforsikringsavggift 8.38 kr/dag for begge
TFA = 8.38
# D er antall dager forsikringen gjelder, her et normalår med 365 dager
D = 365

#Drivstoffforbruk elbil kWh per km
ElDForb = 0.2

#Drivstofforbruk elbil kr per kWh
ElDPris = 2.00

#Drivstofforbruk bensinbil i kr per km
BensinDFP = 1.0

#Bomavgift per km
ElBom = 0.1
BensinBom = 0.3

#Drivstofforbruk elbil i pris per km
ElDFP = ElDForb*ElDPris

Elbilårspris = ElDFP*km + ElFors + ElBom*km + TFA*D

print('Årspris for elbil = ', Elbilårspris, ' kr')

Bensinårspris = BensinDFP*km + BensinFors + BensinBom*km + TFA*D

print('Årspris for bensinbil = ', Bensinårspris, ' kr')

#Differansen mellom prisen for bensinbil og elbil per år er
#Bensinårspris - Elbilårspris (hvor positivt tall betyr at bensinbil er dyrest)

print('Differansen i årspris mellom bensinbil og elbil er ', Bensinårspris - Elbilårspris, ' kr')
