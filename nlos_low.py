import math
import extra_math

def L_rts(f_G,r_h,h_m,h_BD):
    delta_h_m=h_BD-h_m
    return 10*math.log10(f_G)-10*math.log10(r_h)+20*math.log10(delta_h_m)

def correction(r_h,h_m,h_BD):
    delta_h_m=h_BD-h_m
    return 20*math.log10(delta_h_m/7.8)+10*math.log10(20/r_h)

def common(a, b, c, d, e, f, R_k, f_G, delta_h, r_h, h_m, h_BD):
    return (a+b*math.log10(f_G))-(c+d*math.log10(f_G))*extra_math.sgn(delta_h)*math.log10(1+math.fabs(delta_h))+(e-f*extra_math.sgn(delta_h)*math.log10(1+math.fabs(delta_h))*math.log10(R_k))+correction(r_h,h_m,h_BD)+L_rts(f_G,r_h,h_m,h_BD)

def staircase(R_k,f_G,delta_h,r_h,h_m,h_BD):
    return common(137, 35.16, 12.48, 4.16, 39.46, 4.13, R_k, f_G, delta_h, r_h, h_m, h_BD)

def transverse(R_k,f_G,delta_h,r_h,h_m,h_BD):
    return common(139.01, 42.59, 14.97, 4.99, 40.67, 4.57, R_k, f_G, delta_h, r_h, h_m, h_BD)

def lateral(R_k,f_G,delta_h,r_h,h_m,h_BD):
    return common(127.39, 31.63, 13.05, 4.35, 29.18, 6.70, R_k, f_G, delta_h, r_h, h_m, h_BD)