import os
import glob
from time import strftime, gmtime
import fileinput

starttijd = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# De volgorde van deze stappen is belangrijk, voer ze van boven naar beneden uit

# invoermap opgeven
# dir_in = r'E:\Daniel\GITea-checkout\dpigi-TOP10NL-help\Top10NL Help Verkenningsvoorschriften\Content'
# dir_in = r'E:\Daniel\GITea-checkout\test-top10nl-help\verkenningsvoorschriften'
dir_in = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\test-top10nl-help\verkenningsvoorschriften'

#uitvoer bestanden opgeven
# dir_out = r'E:\Daniel\GITea-checkout\test-top10nl-help\todo_daniel\convert' # deze repository
dir_out = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\test-top10nl-help\todo_daniel\convert'  # deze repository laptop

filenaam_snippet_out = (starttijd.replace(" ", "_")).replace(":",".") + "_Snippet-analyse" + ".txt"
filenaam_keyword_out = (starttijd.replace(" ", "_")).replace(":",".") + "_Keyword-analyse" + ".txt"
file_snippet_out = os.path.join(dir_out, filenaam_snippet_out)
file_keyword_out = os.path.join(dir_out, filenaam_keyword_out)

# encoding opgeven
enc = 'utf-8'

# voor een map (in dit geval alleen hoofdmap A)
# for files in glob.glob("**/A.htm", recursive=True):

# voor alleen de hoofd alfabetmappen:
# for files in glob.glob("*/*.htm", recursive=True):

# voor de hele alfabetmap:
# for files in glob.glob("**/*.htm", recursive=True):

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Snippets

# openen uitvoer bestand
f_out = open(file_snippet_out, 'w')

f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Analyse uitgevoerd op: %s\n\n" % (starttijd))
f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Bestandsnaam;Snippet compleet;Snippet\n")

os.chdir(dir_in)
# voor de hele alfabetmap:
for files in glob.glob("**/*.htm", recursive=True):
    file = os.path.join(dir_in, files)
    # print(file, end=" ")
    # invoer bestanden openen
    for regel in fileinput.input(files=[files],openhook=fileinput.hook_encoded("utf-8", "surrogateescape")):
        if "flsnp" in regel:
            snippet = regel.split("\"")[1]
            # print(snippet)
            snip = snippet.split("/")[5]
            # print(snip)
            f_out.write ("%s;%s;%s\n" % (files, snippet, snip))
    fileinput.close()
    # print('  klaar')
       
#sluiten bestanden
f_out.close()
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Keywords

# openen uitvoer bestand
f_out = open(file_keyword_out, 'w')

f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Analyse uitgevoerd op: %s\n\n" % (starttijd))
f_out.write ("--------------------------------------------------------------------------------------------------------------------------------\n\n")
f_out.write ("Bestandsnaam;Titel;Keywords\n")

os.chdir(dir_in)
# voor de hele alfabetmap:
for files in glob.glob("**/*.htm", recursive=True):
    file = os.path.join(dir_in, files)
    # print(file, end=" ")
    # invoer bestanden openen
    for regel in fileinput.input(files=[files],openhook=fileinput.hook_encoded("utf-8", "surrogateescape")):
        if "MadCap:keyword" in regel:
            titelplus = regel.split(">")[1]
            titel = titelplus.split("<")[0]
            keyword = regel.split("\"")[1]
            f_out.write ("%s;%s;%s\n" % (files, titel, keyword))
    fileinput.close()
    # print('  klaar')
       
#sluiten bestanden
f_out.close()
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

# dir_in = r'E:\Daniel\GITea-checkout\dpigi-TOP10NL-help\Top10NL-Help\Content'
# dir_in = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\dpigi-TOP10NL-help\Top10NL-Help\Content'
