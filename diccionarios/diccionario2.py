topics={
    "matemáticas":"mathematics",
    "química":"chemistry",
    "física":"physics",
    "ciencias":"science",
    "ingles":"english"
}
palabra=input("ingrese palabra a traducir")
if palabra in topics.keys():
    print(topics[palabra])

for key,value in topics.items():
    if palabra==value:
        print(key)
