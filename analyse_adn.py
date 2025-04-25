import matplotlib.pyplot as plt
#fonction de lecture de fichier fasta et récupération de la séquence
def lire_fasta():
    fname= input("file name:")
    file=open(fname)
    lines = file.readlines()
    sequence = ""
    for lig in lines:
        #récupérer seulement la ligne de la séquence
        if not lig.startswith('>'):
            sequence += lig.strip() #supprimer les espaces 
            
        
    return sequence.upper()            
  
def calcul_GC(nom_seq):
    #compter le nombre de 'G' et 'C'
    nb_g = nom_seq.count('G')
    nb_c = nom_seq.count('C')
    #somme
    nb_gc = nb_g+nb_c
    #%GC
    gc_content = (nb_gc / len(nom_seq)) * 100
    return gc_content


def freq_nucleotides (nom_seq):
    nucleotides = ['A', 'T', 'C', 'G']
    resultat_freq = []
    #parcourir les nucleotides de la liste
    for i in nucleotides :
        count_nucl = nom_seq.count(i)
        #à chaque comptage, mémoriser le nucleotide et sa fréquence dans une liste
        resultat_freq.append((i, count_nucl))
    return (resultat_freq)

#création barplot de fréquence de nucleotides
def graph():
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    plt.bar(["A", "T", "C", "G"], [a, t, c, g], color=["skyblue", "orange", "green", "purple"])
    plt.title("Fréquence des nucléotides")
    plt.xlabel("Nucléotides")
    plt.ylabel("Nombre d'occurrences")
    graphique = plt.show()
    return graphique

    
    

seq=lire_fasta()
GC_pourcentage = calcul_GC(seq)
freq_nucl = freq_nucleotides (seq)
print("séquence:", seq)
print("%GC égal à :", GC_pourcentage)
print("Fréquence des nucleotides:" , freq_nucl)
plot=graph()











    
    
    
                 



    
