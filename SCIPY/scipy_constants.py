import scipy as sp

print('\n list of scipy constants: ',end='')
print(dir(sp.constants))

# SI units
# Metric Prefix - return unit in meter
print("Yotta      : ",sp.constants.yotta)    #1e+24
print("Zetta      : ",sp.constants.zetta)    #1e+21
print("Exa        : ",sp.constants.exa)      #1e+18
print("Peta       : ",sp.constants.peta)     #1000000000000000.0
print("Tera       : ",sp.constants.tera)     #1000000000000.0
print("Giga       : ",sp.constants.giga)     #1000000000.0
print("Mega       : ",sp.constants.mega)     #1000000.0
print("Kilo       : ",sp.constants.kilo)     #1000.0
print("Hecto      : ",sp.constants.hecto)    #100.0
print("Deka       : ",sp.constants.deka)     #10.0
print("Deci       : ",sp.constants.deci)     #0.1
print("Centi      : ",sp.constants.centi)    #0.01
print("Milli      : ",sp.constants.milli)    #0.001
print("Micro      : ",sp.constants.micro)    #1e-06
print("Nano       : ",sp.constants.nano)     #1e-09
print("Pico       : ",sp.constants.pico)     #1e-12
print("Femto      : ",sp.constants.femto)    #1e-15
print("Atto       : ",sp.constants.atto)     #1e-18
print("Zepto      : ",sp.constants.zepto)    #1e-21

# Length - return unit in meter
print("Inch              : ",sp.constants.inch)              #0.0254
print("Foot              : ",sp.constants.foot)              #0.30479999999999996
print("Yard              : ",sp.constants.yard)              #0.9143999999999999
print("Mile              : ",sp.constants.mile)              #1609.3439999999998
print("Mili              : ",sp.constants.mil)               #2.5399999999999997e-05
print("Point             : ",sp.constants.pt)                #0.00035277777777777776
print("Point             : ",sp.constants.point)             #0.00035277777777777776
print("Survey Foot       : ",sp.constants.survey_foot)       #0.3048006096012192
print("Survey Mile       : ",sp.constants.survey_mile)       #1609.3472186944373
print("Nautical Mile     : ",sp.constants.nautical_mile)     #1852.0
print("Fermi             : ",sp.constants.fermi)             #1e-15
print("Angstrom          : ",sp.constants.angstrom)          #1e-10
print("Micron            : ",sp.constants.micron)            #1e-06
print("Astronomical Unit : ",sp.constants.au)                #149597870691.0
print("Astronomical Unit : ",sp.constants.astronomical_unit) #149597870691.0
print("Light Year        : ",sp.constants.light_year)        #9460730472580800.0
print("Parsec            : ",sp.constants.parsec)            #3.0856775813057292e+16

# Mass - return unit in kilogram
print("Gram        : ",sp.constants.gram)           #0.001
print("Metric Ton  : ",sp.constants.metric_ton)     #1000.0
print("Grain       : ",sp.constants.grain)          #6.479891e-05
print("Pound       : ",sp.constants.lb)             #0.45359236999999997
print("Pound       : ",sp.constants.pound)          #0.45359236999999997
print("Ounce       : ",sp.constants.oz)             #0.028349523124999998
print("Ounce       : ",sp.constants.ounce)          #0.028349523124999998
print("Stone       : ",sp.constants.stone)          #6.3502931799999995
print("Long Ton    : ",sp.constants.long_ton)       #1016.0469088
print("Short Ton   : ",sp.constants.short_ton)      #907.1847399999999
print("Troy Ounce  : ",sp.constants.troy_ounce)     #0.031103476799999998
print("Troy Pound  : ",sp.constants.troy_pound)     #0.37324172159999996
print("Carat       : ",sp.constants.carat)          #0.0002
print("Atomic Mass : ",sp.constants.atomic_mass)    #1.66053904e-27
print("Atomic Mass : ",sp.constants.m_u)            #1.66053904e-27
print("Atomic Mass : ",sp.constants.u)              #1.66053904e-27

# Binary - return unit in bytes
print("Kibi : ",sp.constants.kibi)    #1024
print("Mebi : ",sp.constants.mebi)    #1048576
print("Gibi : ",sp.constants.gibi)    #1073741824
print("Tebi : ",sp.constants.tebi)    #1099511627776
print("Pebi : ",sp.constants.pebi)    #1125899906842624
print("Exbi : ",sp.constants.exbi)    #1152921504606846976
print("Zebi : ",sp.constants.zebi)    #1180591620717411303424
print("Yobi : ",sp.constants.yobi)    #1208925819614629174706176

# Angle - return unit in radians
print("Degree    : ",sp.constants.degree)     #0.017453292519943295
print("Arcminute : ",sp.constants.arcmin)     #0.0002908882086657216
print("Arcminute : ",sp.constants.arcminute)  #0.0002908882086657216
print("Arcsecond : ",sp.constants.arcsec)     #4.84813681109536e-06
print("Arcsecond : ",sp.constants.arcsecond)  #4.84813681109536e-06

# Time - return unit in seconds
print("Minute      : ",sp.constants.minute)      #60.0
print("Hour        : ",sp.constants.hour)        #3600.0
print("Day         : ",sp.constants.day)         #86400.0
print("Week        : ",sp.constants.week)        #604800.0
print("Year        : ",sp.constants.year)        #31536000.0
print("Julian Year : ",sp.constants.Julian_year) #31557600.0

# Pressure - return unit in pascals
print("Atmosphere             : ",sp.constants.atm)         #101325.0
print("Atmosphere             : ",sp.constants.atmosphere)  #101325.0
print("Bar                    : ",sp.constants.bar)         #100000.0
print("Torr                   : ",sp.constants.torr)        #133.32236842105263
print("Millimeter of mercury  : ",sp.constants.mmHg)        #133.32236842105263
print("Pounds per square inch : ",sp.constants.psi)         #6894.757293168361

# Area - return unit in square meters
print("Hectare : ",sp.constants.hectare) #10000.0
print("Acre    : ",sp.constants.acre)    #4046.8564223999992

# Volume - return unit in cubic meters
print("Liter                : ",sp.constants.liter)            #0.001
print("Litre                : ",sp.constants.litre)            #0.001
print("Gallon               : ",sp.constants.gallon)           #0.0037854117839999997
print("Gallon US            : ",sp.constants.gallon_US)        #0.0037854117839999997
print("Gallon Imperial      : ",sp.constants.gallon_imp)       #0.00454609
print("Fluid Ounce          : ",sp.constants.fluid_ounce)      #2.9573529562499998e-05
print("Fluid Ounce US       : ",sp.constants.fluid_ounce_US)   #2.9573529562499998e-05
print("Fluid Ounce Imperial : ",sp.constants.fluid_ounce_imp)  #2.84130625e-05
print("Barrel               : ",sp.constants.barrel)           #0.15898729492799998
print("Barrel               : ",sp.constants.bbl)              #0.15898729492799998

# Speed - return unit in meter per seconds
print("Kilometer per hour : ",sp.constants.kmh)            #0.2777777777777778
print("Meter per hour     : ",sp.constants.mph)            #0.44703999999999994
print("Mach               : ",sp.constants.mach)           #340.5
print("Speed of Sound     : ",sp.constants.speed_of_sound) #340.5
print("Knot               : ",sp.constants.knot)           #0.5144444444444445

# Temperature - return unit in kelvin
print("Celsius    : ",sp.constants.zero_Celsius)      #273.15
print("Fahrenheit : ",sp.constants.degree_Fahrenheit) #0.5555555555555556

# Energy - return unit in joules
print("Electron Volt            : ",sp.constants.eV)            #1.6021766208e-19
print("Electron Volt            : ",sp.constants.electron_volt) #1.6021766208e-19
print("Calorie                  : ",sp.constants.calorie)       #4.184
print("Calorie TH               : ",sp.constants.calorie_th)    #4.184
print("Calorie IT               : ",sp.constants.calorie_IT)    #4.1868
print("Erg                      : ",sp.constants.erg)           #1e-07
print("British Thermal Units    : ",sp.constants.Btu)           #1055.05585262
print("British Thermal Units IT : ",sp.constants.Btu_IT)        #1055.05585262
print("British Thermal Units TH : ",sp.constants.Btu_th)        #1054.3502644888888
print("Ton TNT                  : ",sp.constants.ton_TNT)       #4184000000.0

# Power - return unit in watts
print("Horsepower : ",sp.constants.hp)         #745.6998715822701
print("Horsepower : ",sp.constants.horsepower) #745.6998715822701

# Force - return unit in newton
print("Dyn            : ",sp.constants.dyn)             #1e-05
print("Dyne           : ",sp.constants.dyne)            #1e-05
print("Lbf            : ",sp.constants.lbf)             #4.4482216152605
print("Pound Force    : ",sp.constants.pound_force)     #4.4482216152605
print("Kgf            : ",sp.constants.kgf)             #9.80665
print("Kilogram Force : ",sp.constants.kilogram_force)  #9.80665