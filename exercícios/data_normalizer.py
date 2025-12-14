list_of_incorrect_names = ["ALICE", "BoB", "ChArlie", "DiaNA MARIE"]

corrected_names = [name.title() for name in list_of_incorrect_names]

print(", ".join(corrected_names))