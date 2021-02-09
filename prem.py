import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = 6371 #km

def inner_core_density(radius): #radius is the normalised radius, r=R/a, with a=6371km
    return 13.0885-8.8381*radius**2
def inner_core_Vp(radius):
    return 11.2622-6.3640*radius**2
def inner_core_Vs(radius):
    return 3.6678-4.4475*radius**2
def inner_core_Q(radius): 
    return 84.6, 1327.7
def inner_core(radius):
    return inner_core_density(radius), inner_core_Vp(radius), inner_core_Vs(radius), inner_core_Q(radius)
 
def outer_core_density(radius):
    return 12.5815 - 1.2638*radius - 3.6426*radius**2 - 5.5281*radius**3
def outer_core_Vp(radius):
    return 11.0487 -4.0362*radius + 4.8023*radius**2 - 13.5732*radius**3
def outer_core_Vs(radius):
    return 0. 
def outer_core(radius):   
    return outer_core_density(radius), outer_core_Vp(radius), outer_core_Vs(radius), np.inf, 57823

def lower_mantle_density(radius):
    density = 7.9565 - 6.4761*radius + 5.5283*radius**2 - 3.0807*radius**3
    return density
def lower_mantle_Vp(radius):
    if radius*a<3630:
        Vp = 15.3891 - 5.3181*radius + 5.5242*radius**2 - 2.5514*radius**3        
    elif radius*a < 5600:
        Vp = 24.9520 - 40.4673*radius + 51.4832*radius**2 - 26.6419*radius**3
    elif radius*a <5701:
        Vp = 29.2766 -23.6027*radius +5.5242*radius**2 - 2.5514*radius**3
    return Vp
def lower_mantle_Vs(radius):
    if radius*a<3630:
        Vs = 6.9254 + 1.4672*radius - 2.0834*radius**2 + 0.9783*radius**3        
    elif radius*a < 5600:
        Vs = 11.1671 -13.7818*radius +17.4575*radius**2 -9.2777*radius**3
    elif radius*a <5701:
        Vs = 22.3459 - 17.2473*radius -2.0834*radius**2 +0.9783*radius**3
    return Vs
def lower_mantle_Q(radius):    
    Qmu = 312
    Qkappa = 57823  
    return Qmu, Qkappa
def lower_mantle(radius):
    return lower_mantle_density(radius), lower_mantle_Vp(radius), lower_mantle_Vs(radius), lower_mantle_Q(radius)

def transition_zone_density(radius):
    if radius*a < 5771:
        density = 5.3197 - 1.4836*radius
    elif radius*a < 5971:
        density = 11.2494 -8.0298*radius
    elif radius*a < 6151:
        density = 7.1089 - 3.8045*radius
    return density
def transition_zone_Vp(radius):
    if radius*a < 5771:
        Vp = 19.0957 - 9.8672 *radius
    elif radius*a < 5971:
        Vp = 39.7027 - 32.6166*radius
    elif radius*a < 6151:
        Vp = 20.3926-12.2569*radius
    return Vp
def transition_zone_Vs(radius):
    if radius*a < 5771:
        Vs = 9.9839 - 4.9324*radius
    elif radius*a < 5971:
        Vs = 22.3512 -18.5856*radius
    elif radius*a < 6151:
        Vs = 8.9496-4.4597*radius
    return Vs
def transition_zone_Q(radius):
    Qmu = 143
    Qkappa = 57823
    return Qmu, Qkappa
def transition_zone(radius):   
    return transition_zone_density(radius), \
        transition_zone_Vp(radius), transition_zone_Vs(radius),\
            transition_zone_Q(radius)

def LVZ_density(radius):
    return 2.6910 + 0.6924*radius
def LVZ_isotropic_Vp(radius):
    return 4.1875 + 3.9382*radius
def LVZ_isotropic_Vs(radius):
    return 2.1519 + 2.3481*radius
def LVZ_isotropic(radius):
    return LVZ_density(radius), LVZ_isotropic_Vp(radius), LVZ_isotropic_Vs(radius),  80, 57823

def LID_density(radius):
    return LVZ_density(radius)
def LID_isotropic_Vp(radius):
    return LVZ_isotropic_Vp(radius)
def LID_isotropic_Vs(radius):
    return LVZ_isotropic_Vs(radius)
def LID_isotropic(radius):
    return LID_density(radius), LID_isotropic_Vp(radius), LID_isotropic_Vs(radius),  600, 57823


def crust_density(radius):
    return 2.9
def crust_Vp(radius):
    return 6.8
def crust_Vs(radius):
    return 3.9
def crust(radius):
    return 2.9, 6.8, 3.9, 600, 57823

def ocean_density(radius):
    return 1.020
def ocean_Vp(radius):
    return 1.45
def ocean_Vs(radius):
    return 0.
def ocean(radius):
    return 1.020, 1.45, 0, np.inf, 57823
    
    
def density(x):
    
    radius = x*a
    IC = 1221.5
    OC = 3480.
    LM = 5701
    TZ = 6151
    LVZ = 6291
    LID = 6346.6
    CR = 6368
    
    if radius < IC: 
        return inner_core_density(x)
    elif radius < OC: 
        return outer_core_density(x)
    elif radius<LM:
        return lower_mantle_density(x)
    elif radius<TZ:
        return transition_zone_density(x)
    elif radius<LVZ:
        return LVZ_density(x)
    elif radius<LID:
        return LID_density(x)
    elif radius<CR:
        return crust_density(x)
    else: 
        return ocean_density(x)
    
  
def Vp(x):
    
    radius = x*a
    IC = 1221.5
    OC = 3480.
    LM = 5701
    TZ = 6151
    LVZ = 6291
    LID = 6346.6
    CR = 6368
    
    if radius < IC: 
        return inner_core_Vp(x)
    elif radius < OC: 
        return outer_core_Vp(x)
    elif radius<LM:
        return lower_mantle_Vp(x)
    elif radius<TZ:
        return transition_zone_Vp(x)
    elif radius<LVZ:
        return LVZ_isotropic_Vp(x)
    elif radius<LID:
        return LID_isotropic_Vp(x)
    elif radius<CR:
        return crust_Vp(x)
    else: 
        return ocean_Vp(x)
    
def Vs(x):
    
    radius = x*a
    IC = 1221.5
    OC = 3480.
    LM = 5701
    TZ = 6151
    LVZ = 6291
    LID = 6346.6
    CR = 6368
    
    if radius < IC: 
        return inner_core_Vs(x)
    elif radius < OC: 
        return outer_core_Vs(x)
    elif radius<LM:
        return lower_mantle_Vs(x)
    elif radius<TZ:
        return transition_zone_Vs(x)
    elif radius<LVZ:
        return LVZ_isotropic_Vs(x)
    elif radius<LID:
        return LID_isotropic_Vs(x)
    elif radius<CR:
        return crust_Vs(x)
    else: 
        return ocean_Vs(x)