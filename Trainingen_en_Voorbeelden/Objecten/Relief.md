---
title: Reliëf
last_modified_date: 28-11-2023
layout: page
parent: TOP10NL Objecten
grand_parent: Trainingen en Voorbeelden
has_children: false
has_toc: false
---

Reliëf
======

## Definitie

Object dat tot doel heeft hoogte te representeren.

## Reliëflijnen, hoge en lage taludlijnen en reliëfpunten

![](images/Top10NL_Info_kruisingsvlakken_relief.png)

|     |     |
| --- | --- |
| ![](images/Top10NL_Info_kruisingsvlakken_relieflijn.gif) | Reliëflijn |
| ![](images/Top10NL_Info_kruisingsvlakken_relieflijn_taludhoog.gif) | Hoge taludlijn |
| ![](images/Top10NL_Info_kruisingsvlakken_relief_taludlaag.gif) | Hoge taludlijn |
| ![](images/Top10NL_Info_kruisingsvlakken_reliefpunt.gif) | Reliëfpunt |

Reliëflijnen hebben geen hartlijnen.<br>
Bij elke hoge taludlijn hoort een lage taludlijn.

## Vlakscheidend

Reliëflijnen met attribuut _type reliëf_ = 'steile rand, aardrand' zijn vlakscheidend.

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

De attributen attribuutwaarden van Reliëf zijn te vinden in de [BRT: Catalogus en Productspecificaties](https://kadaster.github.io/imbrt/#57-reliëf).
