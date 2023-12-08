---
title: Spoorbaandeel
last_modified_date: 28-11-2023
layout: page
parent: TOP10NL Objecten
grand_parent: Trainingen en Voorbeelden
has_children: false
has_toc: false
---

Spoorbaandeel
=============

## Definitie

Kleinste functioneel onafhankelijk stukje spoorbaan met gelijkblijvende, homogene eigenschappen en relaties dat er binnen een spoorwegnet wordt onderscheiden.

## Spoorlijnen en spoorpunten

![](images/Info_spoorbaandeel_spoor.png)

|     |     |
| --- | --- |
| ![](images/Info_spoorbaandeel_spoorlijn.gif) | Spoorlijn |
| ![](images/Info_spoorbaandeel_spoorpunt.gif) | Spoorpunt |

Spoorlijnen hebben geen hartlijnen.<br>
Daar waar 2 spoorlijnen elkaar snijden hoort een spoorpunt en zijn de lijnen onderbroken.

## Vlakscheidend

Spoorbaandelen met attribuut _type spoorbaan_ = 'trein' of 'metro' zijn vlakscheidend.

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

De attributen attribuutwaarden van Spoorbaandeel zijn te vinden in de [BRT: Catalogus en Productspecificaties](https://kadaster.github.io/imbrt/#52-spoorbaandeel).
