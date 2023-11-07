import random
import monkdata as m
import dtree
import matplotlib.pyplot as plt

fraction = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
run_num = 100
error_rate_1=[]
error_rate_3=[]

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

for x in fraction:
    err_1=0
    err_3=0
    for i in range(run_num):
        monk1train, monk1val = partition(m.monk1, x)
        t1=dtree.buildTree(monk1train,m.attributes)
        t1_pruned = dtree.allPruned(t1) # is a list of pruned trees
        # use validation dataset to see if the pruned tree is better than original tree
        err1_pruned_val = min(1-dtree.check(tree,monk1val) for tree in t1_pruned)
        if((1-dtree.check(t1,monk1val))<err1_pruned_val):
            print("pruned result is worse than original tree")
            e1=1-dtree.check(t1,m.monk1test)
        else:
            e1=min(1-dtree.check(tree,m.monk1test) for tree in t1_pruned)
            # print("pruned tree is better")
        err_1+=e1

        
        monk3train, monk3val = partition(m.monk3, x)
        t3=dtree.buildTree(monk3train,m.attributes)
        t3_pruned = dtree.allPruned(t3) # is a list of pruned trees
        err3_pruned_val = min(1-dtree.check(tree,monk3val) for tree in t3_pruned)
        if((1-dtree.check(t3,monk3val))<err3_pruned_val):
            print("pruned result is worse than original tree")
            e3=1-dtree.check(t3,m.monk3test)
        else:
            e3=min(1-dtree.check(tree,m.monk3test) for tree in t3_pruned)
            # print("pruned tree is better")
        err_3+=e3

    error_rate_1.append(err_1/run_num)
    error_rate_3.append(err_3/run_num)

print(error_rate_1)

print(error_rate_3)

# Plotting error_rate_1
plt.figure(figsize=(10, 5))
plt.plot(fraction, error_rate_1, marker='o', label='Error Rate for Monk1')
plt.xlabel('Fraction')
plt.ylabel('Error Rate')
plt.title('Error Rate for Monk1')
plt.grid(True)
plt.legend()

# Show the plots
plt.figure(figsize=(10, 5))
plt.plot(fraction, error_rate_3, marker='x', label='Error Rate for Monk3')
plt.xlabel('Fraction')
plt.ylabel('Error Rate')
plt.title('Error Rate for Monk3')
plt.grid(True)
plt.legend()

plt.show()