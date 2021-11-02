def inkine(x2,y2):
    #shifting of origin
#    x2=x2-10
#   y2=y2-10
    #angle of link1
    if (m.pow(L1,2) + (m.pow(x2,2)+ m.pow(y2,2)) - m.pow(L2,2)) / 2 * L1*(m.sqrt(m.pow(x2,2) + m.pow(y2,2))) >1:
        theta1 = m.atan(y2/x2)
        print('th1 error {},{}'.format(x2,y2))
    elif ((m.pow(L1,2) + (m.pow(x2,2)+ m.pow(y2,2)) - m.pow(L2,2)) / 2 * L1*(m.sqrt(m.pow(x2,2) + m.pow(y2,2)))) < -1:
        theta1=m.atan(y2,x2)-m.pi
        print('th1 error {},{}'.format(x2, y2))
    else:
        theta1 = m.atan(y2 / x2) + m.acos((m.pow(L1, 2) + (m.pow(x2, 2) + m.pow(y2, 2)) - m.pow(L2, 2)) / 2 * L1 * (
            m.sqrt(m.pow(x2, 2) + m.pow(y2, 2))))
