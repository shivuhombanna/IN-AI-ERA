# def create_profile(name,age,**exectra):
#     for key,value in exectra.items():
#         print(f"extra for {name},{age}, this is extra {key} is {value}")

# kd=create_profile("shivu",77,hoby="he",helth="houg",hight="5.26")
# print(kd)
# def display_prile(name,*profile):
#     for key in profile:
#         print(f"name is {name}  job is {key} ")

# display_prile("Shivu","editar")


def display_profile(name,age,city,job):
    s="-"
    s=s*25
    print(s)
    print(f" Name: {name} \n Age: {age} \n City: {city} \n Job: {job}")
    print(s)

display_profile("Shivu",20,"davanagere", "ai devop's ")
display_profile("hanumesh",20,"huballi", "ai analitics ")
