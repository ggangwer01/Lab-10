#the authors are Gwyneth and Victoria


stdt= {"Laneman": "Margaret", "Deyoung": "Lily", "Schuler": "Serenity", "Beck": "Olivia", "Hand": "Colleen", "Raycroft": "Anna", "Garcia": "Victoria",  "Gangwer": "Gwyneth", "Webber-Hess": "Mairi", "Litvak": "Aliza",  "Wyatt": "Elizabeth", "Taylor": "Rylee"}

names_dic= {}
for name in stdt:
    if stdt[name] in names_dic:
        names_dic[stdt[name]] +=1
    else:
        names_dic[stdt[name]]=1
print(names_dic)
