#the authors are Gwyneth and Victoria

cpsc_names = ["Margaret1","Laneman1", "Lily2", "Deyoung2", "Serenity3", "Schuler3", "Olivia4", "Beck4", "Collen5","Hand5", "Anna6","Raycroft6", "Victoria7", "GarciaJimenez7","Gwyneth8","Gangwer8", "Mac9","Weber-Hess9", "Aliza10", "Litvak10", "Elizabeth11", "Wyatt11", "Rylee12", "Taylor12"]
cpsc_names[::2]
print(cpsc_names[1::2])
last_name= cpsc_names[1::2]


def first_name_1(names):
    frequency = {}
    for first in names:
        first_letter = first[0]
        if first_letter in frequency:
            frequency[first_letter] += 1
        else:
            frequency[first_letter] = 1
    return frequency
last_name_frequencies = first_name_1(last_name)

print(last_name_frequencies)






