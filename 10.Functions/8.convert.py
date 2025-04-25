def convert(String):
    String=" ".join(sorted(set(String.lower().split())))
    return String
print(convert("Pavish       pandya         pandya   dhaval"))