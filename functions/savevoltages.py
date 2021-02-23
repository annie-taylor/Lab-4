import pickle as p
from functions import cindysfav

def savevoltages(bursts, XYZ, p_electrode2,dz):
    [burst1, burst2, burst3, burst4, burst5, burst6, burst7, burst8, burst9, burst10] = bursts
    [XYZ1, XYZ2, XYZ3, XYZ4, XYZ5, XYZ6, XYZ7, XYZ8, XYZ9, XYZ10] = XYZ
    #S as pickle files
    if dz:
        V1_dz = cindysfav(burst1, XYZ1, p_electrode2)  # slow but fine
        p.dump(V1_dz, open('V1_dz.p', 'wb'))
        del V1_dz
        V2_dz = cindysfav(burst2, XYZ2, p_electrode2)  # slow but fine
        p.dump(V2_dz, open('V2_dz.p', 'wb'))
        del V2_dz
        V3_dz = cindysfav(burst3, XYZ3, p_electrode2)  # slow but fine
        p.dump(V3_dz, open('V3_dz.p', 'wb'))
        del V3_dz
        V4_dz = cindysfav(burst4, XYZ4, p_electrode2)  # slow but fine
        p.dump(V4_dz, open('V4_dz.p', 'wb'))
        del V4_dz
        V5_dz = cindysfav(burst5, XYZ5, p_electrode2)  # slow but fine
        p.dump(V5_dz, open('V5_dz.p', 'wb'))
        del V5_dz
        V6_dz = cindysfav(burst6, XYZ6, p_electrode2)  # slow but fine
        p.dump(V6_dz, open('V6_dz.p', 'wb'))
        del V6_dz
        V7_dz = cindysfav(burst7, XYZ7, p_electrode2)  # slow but fine
        p.dump(V7_dz, open('V7_dz.p', 'wb'))
        del V7_dz
        V8_dz = cindysfav(burst8, XYZ8, p_electrode2)  # slow but fine
        p.dump(V8_dz, open('V8_dz.p', 'wb'))
        del V8_dz
        V9_dz = cindysfav(burst9, XYZ9, p_electrode2)  # slow but fine
        p.dump(V9_dz, open('V9_dz.p', 'wb'))
        del V9_dz
        V10_dz = cindysfav(burst10, XYZ10, p_electrode2)  # slow but fine
        p.dump(V10_dz, open('V10_dz.p', 'wb'))
        del V10_dz
    else:
        V1 = cindysfav(burst1, XYZ1, p_electrode2)  # slow but fine
        p.dump(V1, open('V1.p', 'wb'))
        del V1
        V2 = cindysfav(burst2, XYZ2, p_electrode2)  # "
        p.dump(V2, open('V2.p', 'wb'))
        del V2
        V3 = cindysfav(burst3, XYZ3, p_electrode2)  # "
        p.dump(V3, open('V3.p', 'wb'))
        del V3
        V4 = cindysfav(burst4, XYZ4, p_electrode2)
        p.dump(V4, open('V4.p', 'wb'))
        del V4
        V5 = cindysfav(burst5, XYZ5, p_electrode2)
        p.dump(V5, open('V5.p', 'wb'))
        del V5
        V6 = cindysfav(burst6, XYZ6, p_electrode2)
        p.dump(V6, open('V6.p', 'wb'))
        del V6
        V7 = cindysfav(burst7, XYZ7, p_electrode2)
        p.dump(V7, open('V7.p', 'wb'))
        del V7
        V8 = cindysfav(burst8, XYZ8, p_electrode2)
        p.dump(V8, open('V8.p', 'wb'))
        del V8
        V9 = cindysfav(burst9, XYZ9, p_electrode2)
        p.dump(V9, open('V9.p', 'wb'))
        del V9
        V10 = cindysfav(burst10, XYZ10, p_electrode2)
        p.dump(V10, open('V10.p', 'wb'))
        del V10