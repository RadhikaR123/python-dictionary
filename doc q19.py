#remove duplicate from a dictionary....

sd = {'id1':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},'id2':{'name': ['David'],'class': ['V'],'subject_integration': ['english, math, science']},'id3':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']}}

sd1={}

for k,v in sd.items():
    for i,j in v.items():
        