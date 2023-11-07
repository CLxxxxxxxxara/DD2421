import monkdata as m
import dtree

i=1
for ds in (m.monk1,m.monk2,m.monk3):
    print ("MONK",i)
    for a in m.attributes:
        gain = dtree.averageGain(ds,a)
        print("Information Gain of", a.name,"is:",gain)
    i=i+1