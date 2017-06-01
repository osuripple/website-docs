---
title: "Comment se connecter sur Ripple (Linux)"
reference_version: 3bfc0f4bf02d4629ff2c1fc76d23edde
---
Ce guide est seulement pour se conncter de osu! à Ripple, et ne pas configurer le jeu lui-même. Vous pouvez suivre [ce guide]
(https://gist.github.com/Francesco149/a2f796683a4e5195458f4bb171d88eb0) mettre le jeu en place.

### Modification du fichier hosts
Pour cela, vous devrez modifier votre fichier *hosts*. Pour ce faire, exécutez `nano /etc/hosts` en tant que root / avec sudo..

Lorsque vous l'ouvrez, copiez ce qui suit en bas:

```
163.172.71.251 osu.ppy.sh a.ppy.sh b.ppy.sh c.ppy.sh c1.ppy.sh s.ppy.sh
51.255.90.169 bm6.ppy.sh
```
**CTRL+X** et après **Entrer** pour enrengistrer le ficher.

### Installation du certificat
Téléchargez le certificat en cliquant [*ici*](https://git.zxq.co/ripple/ripple-server-switcher/raw/master/RippleServerSwitcher/Resources/certificate.cer)

Ouvrez la configuration d'Internet Explorer en exécutant `wine control`.

Double-cliquez sur l'icône *Internet Settings*, accédez à l'onglet *Content*, puis cliquez sur le bouton *Certificats...*.

Cliquez sur *Importer*, puis *Suivant*.

Cliquez sur *Parcourir...* puis sélectionnez le certificat Ripple.

Cliquez sur *Suivant*.

Sélectionnez *Placez tous les certificats dans le store suivant*, et cliquez sur *Parcourir*.

Sélectionnez **Autorités de certification racine de confiance** et cliquez sur *OK*.

Cliquez sur *Suivant*, *Terminer*.

Vous devriez recevoir un message indiquant **L'importation a été effectuée avec succès**.

Après cela, vous pouvez démarrer le client et vous connecter avec vos identifiants Ripple.
