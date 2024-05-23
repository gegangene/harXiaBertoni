import math

def common(a,b,c,d,e,f_G,h_b,R_k):
    return a+b*math.log10(f_G)-c*math.log10(h_b)+(d+e*math.log10(h_b))*math.log10(R_k)

def staircase(R_k,f_G,h_b):
    return common(141.40,39.88,1.33,49.97,3.92,f_G,h_b,R_k)

def transverse(R_k,f_G,h_b):
    return common(144.99,19.59,0.66,49.49,3.52,f_G,h_b,R_k)

def lateral(R_k,f_G,h_b):
    return common(135.41,12.49,4.99,46.84,2.34,f_G,h_b,R_k)