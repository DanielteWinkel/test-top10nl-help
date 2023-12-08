---
title: Wegdeel
last_modified_date: 28-11-2023
layout: page
parent: TOP10NL Objecten
grand_parent: Trainingen en Voorbeelden
has_children: false
has_toc: false
---

Wegdeel
=======

## Definitie

Kleinste functioneel onafhankelijk stukje weg met gelijkblijvende, homogene eigenschappen en relaties voor wegverkeer en vliegverkeer te land.

## Wegvlakken, weglijnen, wegpunten

Een wegvlak met attribuut type infrastructuur="kruising" noemen we een **kruisingsvlak**.<br>
Een wegpunt noemen we een **kruisingspunt**.

![](images/info_wegdeel1aangepast.png)

|     |     |
| --- | --- |
| ![](images/Info_wegdeel_wegvlak.gif) | Wegvlak |
| ![](images/Info_wegdeel_weglijn.gif) | Weglijn |
| ![](images/Info_wegdeel_kruisingsvlak.gif) | Kruisingsvlak |
| ![](images/Info_wegdeel_kruisingspunt.gif) | Kruisingspunt |

Daar waar 2 wegvlakken elkaar kruisen hoort een kruisingsvlak.<br>
Daar waar een weglijn een wegvlak kruist hoort geen kruisingsvlak of kruisingslijn.<br>
Daar waar 2 weglijnen elkaar snijden hoort een kruisingspunt.<br>
Daar waar een weg overgaat in een andere (A) hoort geen kruisingsvlak of kruisingspunt.

## Weg-hartlijnen en weg-hartpunten

Bij elk wegvlak of weglijn met type _infrastructuur_ = "verbinding" hoort een hartlijn (gelinkt: [Geometry Linker](../../Esri_ArcGIS/ArcMap/Toolbars/Toolbars.html#geometry-linker)).<br>
Bij elk kruisingsvlak of kruisingspunt hoort een hartpunt (gelinkt: [Geometry Linker](../../Esri_ArcGIS/ArcMap/Toolbars/Toolbars.html#geometry-linker)) en geen hartlijn.<br>
Een hartlijn zoals aangegeven bij C heeft geen relatie met een wegvlak (niet gelinkt).

![](images/info_wegdeel2.png)

|     |     |
| --- | --- |
| ![](images/Top10NL_Info_kruisingsvlakken_hartlijn.png) | Hartlijn |
| ![](images/Info_wegdeel_hartpunt.gif) | Hartpunt |
| ![](images/Info_wegdeel_kruisingspunt_hartpunt.gif) | Kruisingspunt met bijbehorend hartpunt |
| ![](images/Info_wegdeel_kruisingsvlak_hartpunt.gif) | Kruisingsvlak met bijbehorend hartpunt |

Daar waar een weg overgaat in een andere (A) zijn ook de hartlijnen onderbroken.<br>
Daar waar een weg overgaat in een andere (A) hoort geen hartpunt.<br>
Bij een afgesloten weg (B) loopt de hartlijn tot aan de rand van het wegvlak.

## Vlakscheidend

Alle lijnvormige wegdelen zijn vlakscheidend.

Vlakscheidend betekent dat als er een lijnobject een wegvlak, terreinvlak of watervlak doorsnijdt dat het vlak geknipt moet worden op de plaats van de lijn(en).

|     |     |     |     |
| --- | --- | --- | --- |
| ![](images/Info_vlakscheidende_waterlijn_voor.png)          | → | ![](images/Info_vlakscheidende_waterlijn_na.png)          | 1 waterlijn doorsnijdt een terreinvlak |
| ![](images/Info_vlakscheidende_waterlijnen_voor.png)        | → | ![](images/Info_vlakscheidende_waterlijnen_na.png)        | 2 waterlijnen tezamen doorsnijden een terreinvlak |
| ![](images/Info_vlakscheidende_waterlijnen_duiker_voor.png) | → | ![](images/Info_vlakscheidende_waterlijnen_duiker_na.png) | 3 waterlijnen tezamen doorsnijden een terreinvlak |

Het vlak wordt niet opgedeeld als vlakscheidende lijn gedeeltelijk in het terreinvlak steekt:<br>
![](images/Info_vlakscheidende_waterlijn.png)

Het is niet toegestaan dat een vlakscheidende lijn gedeeltelijk in een wegvlak steekt:<br>
![](images/Info_vlakscheidende_waterlijn_in_weg.png)

## Attributen en attribuutwaarden

De attributen attribuutwaarden van Wegdeel zijn te vinden in de [BRT: Catalogus en Productspecificaties](https://kadaster.github.io/imbrt/#51-wegdeel).
