my_family = {
    "wife": {
        "name": "Holly",
        "age": 27
    },
    "mother": {
        "name": "Adrienne",
        "age": 62
    },
    "father": {
        "name": "Doug",
        "age": 62
    },
    "sister1": {
        "name": "Merritt",
        "age": 27
    },
    "sister2": {
        "name": "Madison",
        "age": 25
    },
    "sister3": {
        "name": "Hayden",
        "age": 25
    }
}

father_dict_comp = {k:v for (k, v) in my_family.items() if k == "father"}

print(f"{father_dict_comp['father']['name']} is my {(str(list(father_dict_comp.keys())[0]))} and he is {str(father_dict_comp['father']['age'])} years old")

