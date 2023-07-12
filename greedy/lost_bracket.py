# boj_1541

formula=input()

main_clause=formula.split("-")

first_clause=main_clause[0].split("+")
res=0
for i in first_clause:
    res+=int(i)
for mc in main_clause[1:]:
    plus_clause=mc.split("+")
    res-=sum(list(map(int,plus_clause)))
print(res)