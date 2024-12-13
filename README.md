# JYU Navi yhteenveto

Tarkoituksena on helpottaa tilojen varausten tarkastelua ja löytää avoin opiskelutila mahdollisimman nopeasti.
Ennen tämä täytyin tehdä kartasta klikkailemalla useampi ikkuna auki kerralla ja käymällä ne yksi kerrallaan läpi. 

## Käyttö 

Ohjelma generoi HTML sivun, jota voi tarkastella osoitteessa [http://users.jyu.fi/~tealjapa/navi/](http://users.jyu.fi/~tealjapa/navi/).

```
python generate.py > index.html
```

## Tietorakenne

Tieto tiloista on esitetty seuraavasti:

```
lähde = [["m3406546", 
          "m3406547", 
          "m3406548", 
          "m3406549", 
          "m3406550", 
          "m3406453", 
          "m3406452", 
          "m3406451", 
          "m3406450"],
         ["BP 45.2", 
          "BP 55.2", 
          "BP 55.1", 
          "BYP 45.4", 
          "BYP 45.3", 
          "BYP 45.2", 
          "BYP 45.3", 
          "BYP 45.4", 
          "BYP 45.5"]]

agora = [["m2137966", 
          "m2137961"],
         ["Ag B301",
          "Ag B201"]
``` 
