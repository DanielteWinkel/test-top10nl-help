import os
import glob
from time import strftime, gmtime
import fileinput

print("\nStart\n")

starttijd = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# De volgorde van deze stappen is belangrijk, voer ze van boven naar beneden uit

# invoermap en uitvoerbestand opgeven Verkenningsvoorschriften
dir_in_vv = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\dpigi-TOP10NL-help\Top10NL Help Verkenningsvoorschriften'
filenaam_snippet_out_vv = (starttijd.replace(" ", "_")).replace(":",".") + "_Snippet-analyse_Verkenningsvoorschriften" + ".txt"
filenaam_keyword_out_vv = (starttijd.replace(" ", "_")).replace(":",".") + "_Keyword-analyse_Verkenningsvoorschriften" + ".txt"

# invoermap opgeven TOP10NL-help algemeen
dir_in_help = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\dpigi-TOP10NL-help\Top10NL-Help'
filenaam_snippet_out_help = (starttijd.replace(" ", "_")).replace(":",".") + "_Snippet-analyse_Top10NL-Help" + ".txt"
filenaam_keyword_out_help = (starttijd.replace(" ", "_")).replace(":",".") + "_Keyword-analyse_Top10NL-Help" + ".txt"

# uitvoer map opgeven
dir_out = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\dpigi-TOP10NL-help\todo\convert'  # deze repository laptop
file_snippet_out_vv = os.path.join(dir_out, filenaam_snippet_out_vv)
file_keyword_out_vv = os.path.join(dir_out, filenaam_keyword_out_vv)
file_snippet_out_help = os.path.join(dir_out, filenaam_snippet_out_help)
file_keyword_out_help = os.path.join(dir_out, filenaam_keyword_out_help)

# encoding opgeven
enc = 'utf-8'

# voor een map (in dit geval alleen hoofdmap A)
# for files in glob.glob("**/A.htm", recursive=True):

# voor alleen de hoofd alfabetmappen:
# for files in glob.glob("*/*.htm", recursive=True):

# voor de hele alfabetmap:
# for files in glob.glob("**/*.htm", recursive=True):

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Verkenningsvoorschriften
# --------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Snippets

# openen uitvoer bestand
f_out = open(file_snippet_out_vv, 'w')
dir_in = dir_in_vv

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
            snip = snippet.split("/")
            snip_len = len(snip)
            snipp = snip[(snip_len-1)]
            # print(snipp)
            f_out.write ("%s;%s;%s\n" % (files, snippet, snipp))
    fileinput.close()
    # print('  klaar')
       
#sluiten bestanden
f_out.close()
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Keywords

# openen uitvoer bestand
f_out = open(file_keyword_out_vv, 'w')
dir_in = dir_in_vv

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


# --------------------------------------------------------------------------------------------------------------------------------------------------
# TOP10nl-Help
# --------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Snippets

# openen uitvoer bestand
f_out = open(file_snippet_out_help, 'w')
dir_in = dir_in_help

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
            snip = snippet.split("/")
            snip_len = len(snip)
            snipp = snip[(snip_len-1)]
            # print(snipp)
            f_out.write ("%s;%s;%s\n" % (files, snippet, snipp))
    fileinput.close()
    # print('  klaar')
       
#sluiten bestanden
f_out.close()
    
# --------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Analyseer HTM bestanden op het gebuik van Keywords

# openen uitvoer bestand
f_out = open(file_keyword_out_help, 'w')
dir_in = dir_in_help

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
print("\nKlaar\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------
