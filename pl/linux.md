---
title: "Jak połączyć się z Ripple (Linux)"
reference_version: 2a77df23ecc8f9be75819e98afadcef1
---
Ten przewodnik jest tylko do połączenia osu! z Ripple, nie ustawiania gry do stanu użytku. Możesz użyć [tego przewodnika](https://gist.github.com/Francesco149/a2f796683a4e5195458f4bb171d88eb0) by zainstalować klienta.

### Modyfikowanie pliku hosts
Najpierw musisz zmodyfikować twój pilk *hosts*. By to zrobić, wpisz w terminalu `nano /etc/hosts` jako root/z sudo.

Gdy już otworzyłeś plik, wklej poniższy tekst:

```
{ipmain} osu.ppy.sh a.ppy.sh b.ppy.sh c.ppy.sh c1.ppy.sh s.ppy.sh
{ipmirror} bm6.ppy.sh
```
**CTRL+X** potem **Enter** by zapisać plik.

### Instalowanie certyfikatu
Pobierz certyfikat klikając [*tutaj*](https://git.zxq.co/ripple/ripple-server-switcher/raw/master/RippleServerSwitcher/Resources/certificate.cer)

Otwórz konfigurację Internet Explorer przez uruchamianie `wine control`.

Kliknij podwójnie ikonę *Ustawienia internetu*, przejdź do karty *Zawartość*, wtedy kliknij przycisk *Certyfikaty*.

Wciśnij *Importuj*, wtedy *Dalej*.

Wciśnij *Przeglądaj...* wtedy wybierz certyfikat Ripple'a.

Wciśnij *Dalej*.

Wybierz *Place all certificates in the following store* i wciśnij *Browse*.

Wybierz **Zaufane główne urzędy certyfikacji**, potem wciśnij *Ok*.

Wciśnij *Dalej*, *Zakończ*.

Powinieneś dostać informację **Import został pomyślnie ukończony**.


Po skończeniu importowania certyfikatu, możesz uruchomić klienta, i zalogować się na Ripple'a.
