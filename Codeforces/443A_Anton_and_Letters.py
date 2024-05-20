Letters = list(input())

#removes commas
for a in Letters:
    if a == ",":
        Letters.remove(a)

#removes spaces
Letters = list(filter(str.strip, Letters))

#removes same letters
Letters = "".join(dict.fromkeys(Letters))

print(len(Letters) - 2)