---
title: "Installing the certificate manually"
reference_version: 96a9ef2265cef92f7a7014f3303b74b9
---
Se riscontri dei problemi nel connetterti a Ripple usando la stable (latest)/beta/cuttingedge o lo switcher non installa correttamente il certificato, puoi installare il certificato manualmente.

### Istruzioni
- Per prima cosa, scarica il certificato [cliccando qui](https://git.zxq.co/ripple/ripple-server-switcher/raw/master/RippleServerSwitcher/Resources/certificate.cer)
- In seguito, apri **certificate.cer**
- Clicca **Installa certificato...**
- Clicca **Avanti**
- Seleziona **Posiziona tutti i certificati nel seguente archivio** (seconda opzione), poi clicca **Sfoglia...**
- Spunterà una nuova finestra, seleziona **Autorità di certificazione fonti attendibili** e clicca **Ok**
- Clicca **Avanti**
- Clicca **Fine**

### Come testare il certificato
Per verificare che il certificato sia stato installato con successo, assicurati che lo switcher sia su **On** e apri [questa pagina](https://c.ppy.sh).  

- Se vedi **[cose di osu!bancho](http://y.zxq.co/ubfzty.png)**, il tuo switcher è impostato su off. **Impostalo su on e prova di nuovo.**  
- Se vedi **[delle cose di ripple](http://y.zxq.co/zphobw.png)**, sei connesso a ripple con successo in https, **ottimo!**  
- Se ricevi **[degli errori di certificato o di sicurezza](http://y.zxq.co/reaueu.png)**, il certificato non è stato installato con successo. **Segui le istruzioni sottostanti.**  

### Se qualcos'altro non va a buon fine...
...puoi provare a rimuovere tutti i certificati esistenti di Ripple ed installare il certificato nuovamente. Segui questi passaggi:

- Premi **Win+R**  
- Digita `mmc certmgr.msc` nella finestra esegui e premi **invio** per aprire il Gestore Certificati  
- Seleziona **Autorità di certificazione fonti attendibili** sulla sinistra  
- Seleziona **Certificati** sulla destra  
- Dovresti vedere una voce di **[Ripple](http://y.zxq.co/bbyxev.png)** ed una o due voci **\*.ppy.sh** nella lista. Selezionale, **click destro** e clicca su **Rimuovi**  
- Seleziona tutte le opzioni positive  
- Apri lo switcher, clicca su **Install certificate**, poi **Sì**  
- Prova a connetterti al [server bancho di ripple in https](https://c.ppy.sh/) e _dovrebbe_ funzionare
