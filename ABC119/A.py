from datetime import datetime as dt

tstr = input()
tdatetime = dt.strptime(tstr, '%Y/%m/%d')

if tdatetime <= dt.strptime('2019/04/30', '%Y/%m/%d') :
    print('Heisei')
else :
    print('TBD')
