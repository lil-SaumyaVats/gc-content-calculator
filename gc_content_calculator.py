dna = input("Enter a DNA sequence: ")
dna = dna.upper()
if dna == "":
    print("Please enter a DNA sequence")
    exit()
for letter in dna:
    if letter not in "ATGC":
        print("Invalid DNA sequence")
        exit()
print("Valid DNA sequence")
total_bases = len(dna)
g_count = dna.count("G")
c_count = dna.count("C")
gc_count = g_count + c_count

gc_content = (gc_count / total_bases) * 100

print("Total bases:", total_bases)
print("G_count:", g_count)
print("C_count:", c_count)
print(f"GC_content: {gc_content:.2f}%")



