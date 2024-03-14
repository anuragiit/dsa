def permute(list_,a,permutations_):
    len_=len(list_)
    if a==len_:
        permutations_.append(''.join(list_)) # be careful when the question is for list instead of string,in that case we need to
    else:                                                       # take a copy of the modified list and only then add to permutations list, else it will modify all already inserted permutations
        look_up=set()
        for i in range(a,len_):
            if list_[i] not in look_up:
               list_[i],list_[a]=list_[a],list_[i]
               permute(list_,a+1,permutations)
               list_[i],list_[a]=list_[a],list_[i]
               look_up.add(list_[i])

t=int(input())
for i in range(t):
    a=input()
    permutations=list()
    permute(list(a),0,permutations)
    print(permutations,'\n',len(permutations))
