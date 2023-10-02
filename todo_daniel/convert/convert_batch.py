import os
import glob
import fileinput

# De volgorde van deze stappen is belangrijk, voer ze van boven naar beneden uit

# invoermap opgeven
# dir_in = r'E:\Daniel\GITea\test-top10nl-help\verkenningsvoorschriften'
dir_in = r'C:\Users\WinkelDanielte\OneDrive - Kadaster\_GITea_intern\test-top10nl-help\verkenningsvoorschriften'
datum = "19-09-2023"

# # voor markdownify en html2text op 
# scriptplek = r'C:\Users\winked\AppData\Roaming\Python\Python39\Scripts'
# mkdwn = os.path.join(scriptplek, 'markdownify')
# ht2txt = os.path.join(scriptplek, 'html2text')

# voor een map (in dit geval alleen hoofdmap A)
# for files in glob.glob("**/A.htm", recursive=True):

# voor alleen de hoofd alfabetmappen:
# for files in glob.glob("*/*.htm", recursive=True):

# voor de hele alfabetmap:
# for files in glob.glob("**/*.htm", recursive=True):

# # --------------------------------------------------------------------------------------------------------------------------------------------------
# # Creeer lege MD-file voor de hoofd-alfabet-html's en vul deze met basisgegevens
# os.chdir(dir_in)
# # voor alleen de hoofd-alfabetmappen:
# for files in glob.glob("*/*.htm", recursive=True):
#     # print(files)
#     file = os.path.join(dir_in, files)
#     print(file)
#     dest = os.path.join(dir_in, files.split(".")[0]) + ".md"
#     # print(dest)
#     filessplit = files.split("\\")
#     if len(filessplit) == 2:
#         titel = str((files.split("\\")[1]).split(".")[0])
#     elif len(filessplit) == 3:
#         titel = str((files.split("\\")[2]).split(".")[0])
#     # print(titel)
#     titel_isjes = "=" * len(titel)
   
#     # alleen aanmaken als MD_bestand nog niet bestaat
#     if os.path.exists(dest):
#         print('MD-bestand bestaat al')
#     else:
#         # aanmaken MD-file
#         f = open(dest, 'w')
       
#         f.write ("---\n")
#         f.write ("title: %s\n" % (titel))
#         f.write ("last_modified_date: %s\n" % (datum))
#         f.write ("layout: page\n")
#         f.write ("parent: Verkenningsvoorschriften\n")
#         f.write ("has_children: true\n")
#         f.write ("has_toc: false\n")
#         f.write ("---\n")
#         f.write ("\n")
#         f.write ("| [A](../A/A.html) | [B](../B/B.html) | [C](../C/C.html) | [D](../D/D.html) | [E](../E/E.html) | [F](../F/F.html) |\n")
#         f.write ("| [G](../G/G.html) | [H](../H/H.html) | [I](../I/I.html) | [J](../J/J.html) | [K](../K/K.html) | [L](../L/L.html) |\n")
#         f.write ("| [M](../M/M.html) | [N](../N/N.html) | [O](../O/O.html) | [P](../P/P.html) | [R](../R/R.html) | [S](../S/S.html) |\n")
#         f.write ("| [T](../T/T.html) | [U](../U/U.html) | [V](../V/V.html) | [W](../W/W.html) | [Z](../Z/Z.html) |\n")
#         f.write ("\n")
#         f.write ("%s\n" % (titel))
#         f.write ("%s\n" % (titel_isjes))
#         f.write ("\n")
        
#         f.close()
# # --------------------------------------------------------------------------------------------------------------------------------------------------

# # --------------------------------------------------------------------------------------------------------------------------------------------------
# # Creeer lege MD-file voor de pagina-html's en vul deze met basisgegevens
# os.chdir(dir_in)
# # voor de hele alfabetmap:
# for files in glob.glob("**/*.htm", recursive=True):
#     # print(files)
#     file = os.path.join(dir_in, files)
#     print(file)
#     dest = os.path.join(dir_in, files.split(".")[0]) + ".md"
#     # print(dest)
#     # selecteer de bestandsnaam zonder extentie
#     filessplit = files.split("\\")
#     if len(filessplit) == 2:
#         titel = str((files.split("\\")[1]).split(".")[0])
#     elif len(filessplit) == 3:
#         titel = str((files.split("\\")[2]).split(".")[0])
#     # print(titel)
#     titel_isjes = "=" * len(titel)
#     parent = str(files.split("\\")[0])
#     # print(parent)

#     # aanmaken MD-file
#     f = open(dest, 'w')

#     f.write ("---\n")
#     f.write ("title: %s\n" % (titel))
#     f.write ("last_modified_date: %s\n" % (datum))
#     f.write ("layout: page\n")
#     f.write ("grand_parent: Verkenningsvoorschriften\n")
#     f.write ("parent: %s\n" % (parent))
#     f.write ("has_children: false\n")
#     f.write ("---\n")
#     f.write ("\n")
#     f.write ("%s\n" % (titel))
#     f.write ("%s\n" % (titel_isjes))
#     f.write ("\n")
    
#     f.close()
# # --------------------------------------------------------------------------------------------------------------------------------------------------

# # --------------------------------------------------------------------------------------------------------------------------------------------------
# # rename bestandsnaam: spatie naar underscore
# os.chdir(dir_in)
# count = 0
# # voor de hele alfabetmap:
# for files in glob.glob("**/*.*", recursive=True):
#     # print(files)
#     file = os.path.join(dir_in, files)
#     # print(file)
#     # selecteer de bestandsnaam
#     filessplit = files.split("\\")
#     if len(filessplit) == 1:
#         filenaam = str(files.split("\\")[0])
#     elif len(filessplit) == 2:
#         filenaam = str(files.split("\\")[1])
#     elif len(filessplit) == 3:
#         filenaam = str(files.split("\\")[2])
#     # print(filenaam)
#     # in onderstaande volgorde renamen
#       # vervang ' ' door '_'
#       # vervang ',' door '_'
#       # vervang '__' door '_' (2 keer uitvoeren)
#     if ' ' in filenaam:
#         # print(filenaam)
#         filenaamnew = filenaam.replace(" ", "_")
#         # print(filenaamnew)
#         if len(filessplit) == 1:
#             filenew = os.path.join(dir_in, filenaamnew)
#         elif len(filessplit) == 2:
#             filenew = os.path.join(dir_in, filessplit[0], filenaamnew)
#         elif len(filessplit) == 3:
#             filenew = os.path.join(dir_in, filessplit[0], filessplit[1], filenaamnew)
#         print(file)
#         print(filenew)
#         count = count + 1
#         #os.rename(file, filenew)
    
# print(count)
# # --------------------------------------------------------------------------------------------------------------------------------------------------

# # --------------------------------------------------------------------------------------------------------------------------------------------------
# # rename folder: spatie naar underscore
# os.chdir(dir_in)
# count = 0
# # voor de hele alfabetmap:
# rootdir = dir_in
# for rootdir, dirs, files in os.walk(rootdir):
#     for subdir in dirs:
#         dirnaam = os.path.join(rootdir, subdir)
#         # # in onderstaande volgorde renamen
#         #   # vervang ' ' door '_'
#         #   # vervang ',' door '_'
#         #   # vervang '__' door '_' (2 keer uitvoeren)
#         if ' ' in subdir:
#             print(subdir)
#             print(dirnaam)
#             dirnaamnew = dirnaam.replace(" ", "_")
#             print(dirnaamnew)
#             count = count + 1
#             # os.rename(dirnaam, dirnaamnew)
    
# print(count)
# # --------------------------------------------------------------------------------------------------------------------------------------------------
