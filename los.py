import math

def away(R_k,R_bk,f_G,h_b,h_m):
    return (48.38-32.1*math.log10(R_bk))+45.70*math.log10(f_G)+(25.34-13.90*math.log10(R_bk))*math.log10(h_b)+(32.10+13.90*math.log10(h_b))*math.log10(R_k)+20*math.log10(1.6/h_m)

def near(R_k,f_G,h_b):
    return 81.14+39.40*math.log10(f_G)-0.09*math.log10(h_b)+(15.80-5.73*math.log10(h_b))*math.log10(R_k)