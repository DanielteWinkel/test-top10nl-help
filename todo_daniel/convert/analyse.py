import os
import glob
from time import strftime, gmtime
import fileinput

starttijd = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# De volgorde van deze stappen is belangrijk, voer ze van boven naar beneden uit

# invoermap opgeven
dir_in = r'E:\Daniel\GITea-checkout\dpigi-TOP10NL-help\Top10NL Help Verkenningsvoorschriften\Content'

#uitvoer bestanden opgeven
dir_out = r'E:\Daniel\GITea-checkout\test-top10nl-help\todo_daniel\convert' #deze repository
filenaam_out = "Snippet-analyse_" + (starttijd.replace(" ", "_")).replace(":",".") + ".txt"
file_out = os.path.join(dir_out, filenaam_out)

# voor een map (in dit geval alleen hoofdmap A)
# for files in glob.glob("**/A.htm", recursive=True):

# voor alleen de hoofd alfabetmappen:
# for files in glob.glob("*/*.htm", recursive=True):

# voor de hele alfabetmap:
# for files in glob.glob("**/*.htm", recursive=True):

#openen uitvoer bestand
f_out = open(file_out, 'w')

f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Analyse uitgevoerd op: %s\n\n" % (starttijd))
f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Path;Bestandsnaam;Snippet\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Snippets
os.chdir(dir_in)
# voor de hele alfabetmap:
for files in glob.glob("**/*.htm", recursive=True):
    file = os.path.join(dir_in, files)
    print(file, end=" ")
    # invoer bestanden openen
    for regel in fileinput.input([files]):
        element = regel.split()
        snippet = 'test'
    fileinput.close()
    print('  klaar')
    f_out.write ("%s;%s;%s\n" % (dir_in, bestandsnaam, snippet))
       
    
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

#sluiten bestanden
f_out.close()

# dir_in = r'E:\Daniel\GITea-checkout\dpigi-TOP10NL-help\Top10NL-Help\Content'
