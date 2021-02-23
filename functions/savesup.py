import pickle as p
from functions import superposition

def savesup(dz):
    if dz:
        sup1_dz = superposition(p.load(open('V1_dz.p', 'rb')))
        p.dump(sup1_dz, open('sup1_dz.p', 'wb'))
        del sup1_dz
        sup2_dz = superposition(p.load(open('V2_dz.p', 'rb')))
        p.dump(sup2_dz, open('sup2_dz.p', 'wb'))
        del sup2_dz
        sup3_dz = superposition(p.load(open('V3_dz.p', 'rb')))
        p.dump(sup3_dz, open('sup3_dz.p', 'wb'))
        del sup3_dz
        sup4_dz = superposition(p.load(open('V4_dz.p', 'rb')))
        p.dump(sup4_dz, open('sup4_dz.p', 'wb'))
        del sup4_dz
        sup5_dz = superposition(p.load(open('V5_dz.p', 'rb')))
        p.dump(sup5_dz, open('sup5_dz.p', 'wb'))
        del sup5_dz
        sup6_dz = superposition(p.load(open('V6_dz.p', 'rb')))
        p.dump(sup6_dz, open('sup6_dz.p', 'wb'))
        del sup6_dz
        sup7_dz = superposition(p.load(open('V7_dz.p', 'rb')))
        p.dump(sup7_dz, open('sup7_dz.p', 'wb'))
        del sup7_dz
        sup8_dz = superposition(p.load(open('V8_dz.p', 'rb')))
        p.dump(sup8_dz, open('sup8_dz.p', 'wb'))
        del sup8_dz
        sup9_dz = superposition(p.load(open('V9_dz.p', 'rb')))
        p.dump(sup9_dz, open('sup9_dz.p', 'wb'))
        del sup9_dz
        sup10_dz = superposition(p.load(open('V10_dz.p', 'rb')))
        p.dump(sup10_dz, open('sup10_dz.p', 'wb'))
        del sup10_dz
    else:
        sup1 = superposition(p.load(open('V1.p', 'rb')))
        p.dump(sup1, open('sup1.p', 'wb'))
        del sup1
        sup2 = superposition(p.load(open('V2.p', 'rb')))
        p.dump(sup2, open('sup2.p', 'wb'))
        del sup2
        sup3 = superposition(p.load(open('V3.p', 'rb')))
        p.dump(sup3, open('sup3.p', 'wb'))
        del sup3
        sup4 = superposition(p.load(open('V4.p', 'rb')))
        p.dump(sup4, open('sup4.p', 'wb'))
        del sup4
        sup5 = superposition(p.load(open('V5.p', 'rb')))
        p.dump(sup5, open('sup5.p', 'wb'))
        del sup5
        sup6 = superposition(p.load(open('V6.p', 'rb')))
        p.dump(sup6, open('sup6.p', 'wb'))
        del sup6
        sup7 = superposition(p.load(open('V7.p', 'rb')))
        p.dump(sup7, open('sup7.p', 'wb'))
        del sup7
        sup8 = superposition(p.load(open('V8.p', 'rb')))
        p.dump(sup8, open('sup8.p', 'wb'))
        del sup8
        sup9 = superposition(p.load(open('V9.p', 'rb')))
        p.dump(sup9, open('sup9.p', 'wb'))
        del sup9
        sup10 = superposition(p.load(open('V10.p', 'rb')))
        p.dump(sup10, open('sup10.p', 'wb'))
        del sup10
