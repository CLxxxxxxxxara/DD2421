import monkdata as m
import dtree


for x in [1,2,3,4]:
    subset1=dtree.select(m.monk1,m.attributes[4],x)
    print("when a5 is",x)
    for a in m.attributes:
        gain = dtree.averageGain(subset1,a)
        print("Information Gain of", a.name,"is:",gain)

print("-------------------------------------------------------------------------")

subset1=dtree.select(m.monk1,m.attributes[4],1) #select a5=1
print("When a5 = 1: ")
print(dtree.mostCommon(subset1))
print()


subset2=dtree.select(m.monk1,m.attributes[4],2) #select a5=2
print("When a5 = 2: ")
subset2_1=dtree.select(subset2,m.attributes[3],1)
print("a4 = 1: ")
print(dtree.mostCommon(subset2_1))
subset2_2=dtree.select(subset2,m.attributes[3],2)
print("a4 = 2: ")
print(dtree.mostCommon(subset2_2))
subset2_3=dtree.select(subset2,m.attributes[3],3)
print("a4 = 3: ")
print(dtree.mostCommon(subset2_3))
print()

subset3=dtree.select(m.monk1,m.attributes[4],3) #select a5=3
print("When a5 = 3: ")
subset3_1=dtree.select(subset3,m.attributes[5],1)
print("a6 = 1: ")
print(dtree.mostCommon(subset3_1))
subset3_2=dtree.select(subset3,m.attributes[5],2)
print("a6 = 2: ")
print(dtree.mostCommon(subset3_2))

print()

subset4=dtree.select(m.monk1,m.attributes[4],4) #select a5=4
print("When a5 = 4: ")
subset4_1=dtree.select(subset4,m.attributes[0],1)
print("a1 = 1: ")
print(dtree.mostCommon(subset4_1))
subset4_2=dtree.select(subset4,m.attributes[0],2)
print("a1 = 2: ")
print(dtree.mostCommon(subset4_2))
subset4_3=dtree.select(subset4,m.attributes[0],3)
print("a1 = 3: ")
print(dtree.mostCommon(subset4_3))
print("-------------------------------------------------------------------------")

t1=dtree.buildTree(m.monk1,m.attributes,2)
print("Error rate of monk1 is:",1-dtree.check(t1,m.monk1))
print("Error rate of monk1-test is:",1-dtree.check(t1,m.monk1test))

t2=dtree.buildTree(m.monk2,m.attributes)
print("Error rate of monk2 is:",1-dtree.check(t2,m.monk2))
print("Error rate of monk2-test is:",1-dtree.check(t2,m.monk2test))

t3=dtree.buildTree(m.monk3,m.attributes)
print("Error rate of monk3 is:",1-dtree.check(t3,m.monk3))
print("Error rate of monk3-test is:",1-dtree.check(t3,m.monk3test))
print("-------------------------------------------------------------------------")

import drawtree_qt5 as qt5
qt5.drawTree(t1)
#qt5.drawTree(t2)
#qt5.drawTree(t3)