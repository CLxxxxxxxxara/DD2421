import monkdata as m
import dtree

entropy_m1=dtree.entropy(m.monk1)
print("Entropy of MONK1: ",entropy_m1)

entropy_m2=dtree.entropy(m.monk2)
print("Entropy of MONK2: ",entropy_m2)

entropy_m3=dtree.entropy(m.monk3)
print("Entropy of MONK3: ",entropy_m3)