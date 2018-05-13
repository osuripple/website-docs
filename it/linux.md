---
title: "Come connettersi a Ripple (Linux)"
reference_version: 2a77df23ecc8f9be75819e98afadcef1
---
Questa guida serve solo per connettere osu! a ripple, e non ad impostare il gioco in se. Puoi seguire [questa guida](https://gist.github.com/Francesco149/a2f796683a4e5195458f4bb171d88eb0) per l'impostazione del client.

### Modificare il file hosts
Per questo, dovrai modificare il tuo file *hosts*. Per farlo, esegui `nano /etc/hosts` come root o con sudo.

Quando l'hai aperto, incolla quello che segue in fondo:

```
{ipmain} osu.ppy.sh a.ppy.sh b.ppy.sh c.ppy.sh c1.ppy.sh s.ppy.sh
{ipmirror} bm6.ppy.sh
```
**CTRL+X** e poi **Enter** per salvare il file.

### Installare il certificato
Scarica il certificato cliccando [*qui*](https://git.zxq.co/ripple/ripple-server-switcher/raw/master/RippleServerSwitcher/Resources/certificate.cer)

Apri la configurazione dell'Internet Explorer eseguendo il comando `wine control`.

Doppio click sull'icona *Impostazioni Internet*, vai sulla tab *Contenuto*, poi clicca il pulsante *Certificati...*.

Clicca su *Importa*, poi *Avanti*.

Clicca *Sfoglia...* poi seleziona il certificato di Ripple.

Clicca *Avanti*.

Seleziona *Posiziona tutti i certificati nel seguente archivio*, e clicca *Sfoglia*.

Seleziona **Autorità di certificazione radice attendibili**, e clicca *Ok*.

Clicca *Avanti*, *Fine*.

Dovresti ricevere un messaggio che dice **Importazione avvenuta con successo**.


Dopo che ciò è stato fatto, puoi avviare il client, ed accedere con le tue credenziali di Ripple.
