def translate(strand):
    if strand == []:
        return []
    
    codons = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}
    
    proteins = []
    codon = ""

    for n, i in enumerate(strand, 1):
        if n % 3 == 0:
            codon += i
            
            if not (codon in codons):
                raise ValueError("Invalid codon")
            elif codons[codon] == "STOP":
                return proteins
            else:
                proteins.append(codons[codon])

            codon = ""
        else:
            codon += i

    if codon != "":
        raise ValueError("Invalid codon")
    
    return proteins


print(translate("UUCUUCUAAUGGU"))