---
title: Esri ArcMap
last_modified_date: 21-11-2023
layout: page
has_children: true
has_toc: true
---

Esri ArcMap
===========

![](../ArcGis_200x200.png)

Hieronder wordt ten eerste het proces van het editen binnen ArcMap van begin tot eind doorlopen.<br>
Er is een breed scala aan voorbeelden, naslagwerk en opleidingsmateriaal voor Arc-Map beschikbaar:

|     |     |
| --- | --- |  
| [Online Trainingen](Trainingen/Trainingen.html) | Hier word er per onderwerp uitleg gegeven . |
| [Toolbars](Toolbars/Toolbars.html) | Hier vind je een uitleg over de werking van de verschillende toolbars aanwezig in TOP10NL. |
| [Voorbeelden van eenvoudige praktijksituaties](Voorbeelden_eenvoudig/Voorbeelden_eenvoudig.html) | Hierin is een beschrijving toegevoegd om enkele basis handelingen uit te voeren. |
| [Voorbeelden van praktijksituaties](Voorbeelden_geavanceerd/Voorbeelden_geavanceerd.html) | Hier vind je enkele uitgewerkte situaties. |

## Het Editing proces

### Starten van het editing proces
De bewerking van de TOP10NL vindt altijd plaats vanuit een van te voren gedefinieerde taak in de ArcGisWork Flowmanager. Zie hiervoor [Workflow Manager](Esri_Workflowmanager/Esri_Workflowmanager.html).

Het kan hierbij zijn dat er gebruik moet worden gebruikt van Espa.<br>
Voor uitleg hierover zie [Espa](../../Beeldmateriaal/Espa/Espa.html).

Nadat vanuit de Workflow Manager een job is opgestart dient de gebruiker eerst een edit-sessie te starten om wijzigingen aan te kunnen brengen.

Een overzicht van de start- en stopknoppen in ArcGis:<br>
![](Toolbars/TOP10NL_Editing_Environment/start_stop_save_edit.JPG)

### Instellingen
Voor je begint met objecten bewerken is het verstandig enkele dingen in te stellen, zie hiervoor [Instellingen](Arc-Map/Instellingen.htm).

### Voortgang

|     |     |
| --- | --- |
| ![](Trainingen/Voortgang/Voortgang_grid_cel_checked.png) | De voortgang kun je bijhouden door het plaatsen van een voortgangsgrid. In tegenstelling tot vroeger wordt je voortgangsgrid niet meer opgeslagen in het mapdocument (mxd bestand) maar in de database. Bij een reset_mxd ben je dan ook niet meer je voortgangsgrid kwijt.<br>De voortgang is beschikbaar zolang je WMX job bestaat.<br>Een grid bestaat uit meerdere cellen, die elk afzonderlijk gemarkeerd kunnen worden als zijnde 'gereed'.<br>Tijdens het wijzigen van de status van een cel wordt de gewijzigde status in de database opgeslagen.<br>Voor het beheren van de voorgang zijn speciale tools aanwezig in een toolbar. |

#### Voortgangsgrid aan- aan en uitzetten

|     |     |     |
| --- | --- | --- |
| 1   | Klik de knop _Voortgang: grid aan- en uitzetten_ | ![](Toolbars/TOP10NL_Review/aan_en_uitzetten_voortgangsgrid.png) |
| 2   | Klik de knop _Voortgang Aoi grid aan/uit_: hiermee toon je het grid.<br>Nog één keer data op de knop maakt het grid onzichtbaar.<br>Deze valt precies binnen de AOI. | ![](Trainingen/Voortgang/voortgangsgrid_aan_uit.png) |

#### Status van een grid cel wijzigen

|     |     |     |
| --- | --- | --- |
| 1   | Klik de knop Voortgang: gereed | ![](Toolbars/TOP10NL_Review/Review_Grid_gereed.png) |
| 2   | Klik in een cel om de status te wijzigen in 'gereed' | ![](Trainingen/Voortgang/Voortgang_grid_cel_unchecked.png) → ![](Trainingen/Voortgang/Voortgang_grid_cel_checked1.png) |
| 3   | Nogmaals klikken in de cel wijzigt de status weer in 'niet gereed' | ![](Trainingen/Voortgang/Voortgang_grid_cel_checked2.png) → ![](Trainingen/Voortgang/Voortgang_grid_cel_unchecked1.png) |
| 4   | Tijdens het wijzigen van een cel wordt wordt de status in de database opgeslagen middels een automatische save. | |
| 5   | Als je een groep gridcellen gereed wilt maken 'trek' je een kader over deze lege gridcellen.<br>Gereedmeldingen ongedaan maken doe je door weer een data te geven op de cel of cellen | ![](Trainingen/Voortgang/voortgangsgrid_meerdere_cellen_tegelijk.png) |

### Bewerken
Het bewerken van deTOP10NL kent verschillende stadia. Klik op de desbetreffende button voor meer informatie.<br>
Zie hiervoor de [Online Trainingen](Trainingen/Trainingen.html).

### Opslaan
Voor het opslaan van wijzigingen zie:<br>
![](Toolbars//TOP10NL_Editing_Environment/start_stop_save_edit.JPG)

### Controleren & Valideren
Er zijn hiervoor handleidingen beschikbaar zoals: [Nabewerken](https://hetkadaster.sharepoint.com/sites/gd-odr/1e20b/Topografie/handleidingen/1-Processtappen%20TOP10NL/Actueel/5-Nabewerken) en [Validaties en Gaten](https://hetkadaster.sharepoint.com/sites/gd-odr/1e20b/Topografie/handleidingen/1-Processtappen%20TOP10NL/Actueel/7-Validaties%20en%20gaten).

#### Query & Browse:
Query&Browse is een tool voor het opsporen van fouten ten behoeve van het validatieproces.

De Query & Browsetool is beschikbaar via ![](Toolbars/TOP10NL_Validate/Query_en_Browse.png) op de Toolbar [TOP10NL Validate](Toolbars/TOP10NL_Validate.html).

Deze tool en de bijbehorende queries zijn een samenvoeging van de bestaande Query & Browse en zelfontwikkelde nabewerkingscontroles welk speciaal zijn ontwikkeld voor het validatie proces en aangepast voor het verwerken van herzieningsmutaties volgens het Lean proces.

|     |     |
| --- | --- |  
| ![](Trainingen/Controle_en_Validatie/Q_en_B_dialog1_540x329.png) | Na het klikken op het toolbaricoontje ![](Toolbars/Toolbars/TOP10NL_Validate/Query__amp__Browse.png) verschijnt het volgende scherm. |
| ![](Trainingen/Controle_en_Validatie/Q_en_B_dialog.png) | Als eerste dient de fase gekozen worden.<br>Na het klikken op het selectiepijltje in het Query-veld wordt de lijst geopend met voorgedefinieerde queries . |
| ![](Trainingen/Controle_en_Validatie/Result_query_ui.png) | Nadat de gewenste query is geselecteerd kan de query middels de Uitvoeren-knop gestart worden.<br>Het resultaat van de query wordt in het resultaatveld getoond. |
| ![](Trainingen/Controle_en_Validatie/ui_klikken.png) | De gebruiker kan nu op deze resultatenklikken.<br>Afhankelijk van de gekozen actie onderin het scherm zal de applicatie nu naar het gekozen object Pannen, inzoomen (Zoom) of inzoomen met een randje erom heen (Zoom+). |
| ![](Trainingen/Controle_en_Validatie/ui_subquery_selectie.png) | Voor sommige queries zijn ook subqueries gedefinieerd.<br>Na het klikken op het pijltje in het subqueryveld wordt de lijst met subqueries getoond. |
| ![](Trainingen/Controle_en_Validatie/ui_result_subquery.png) | Na geklikt te hebben op de subquery verschijnt het resultaat in het resultaatveld eronder . |

#### Valideren
Zodra je wijzigingen aanbrengt aan objecten moet je een keer valideren.

Je mag ten alle tijden tussentijds valideren, maar om je taak af te ronden moet je valideren en mogen er geen attribuutfouten en topologiefouten meer aanwezig zijn.

> Bij validaties mag geen gebruik gemaakt worden van de mapcache.

Wordt toch de mapcache voor validaties gebruikt dan is de kans groot dat het validatieproces niet de volledige lijst met gevonden fouten toont

Valideren bestaat uit 2 delen:

1. [Attribuut](Trainingen/Controle_en_Validatie/AttribuutValidaties.pdf), zie hiervoor ook [Attributen valideren](Toolbars/TOP10NL_Validate.html#attributen-valideren)
2. [Topologievalidatie](Trainingen/Controle_en_Validatie/TopologyValidaties.pdf), zie hiervoor ook [Topologie valideren](Toolbars/TOP10NL_Validate.html#topologie-valideren).

> Zodra je een object wijzigt, vorm of attribuut, moet je opnieuw valideren.

### Data toevoegen
In ArcMap is het mogelijk data/layers toe te voegen m.b.v. van de standaard Add Data ![](Trainingen/Instellingen/AddData.png) button.

Het tijdelijk toevoegen van BRT-bladwijzers (*.lyr bestand) zijn in het volgende pad te vinden:<br>

[P:\\Sector\_Voorbewerking\\Bladwijzers\\\_Layers\_Bladwijzers\_BRT\](file:///P:/Sector_Voorbewerking/Bladwijzers/_Layers_Bladwijzers_BRT/bladwijzer_10000.lyr)
