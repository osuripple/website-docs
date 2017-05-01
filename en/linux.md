---
title: "How to connect to Ripple (Linux)"
old_id: 14
---
This guide is only for connecting osu! to ripple, and not setting the game itself up. You can follow [this guide](https://gist.github.com/Francesco149/a2f796683a4e5195458f4bb171d88eb0) to set the client up.

### Modifying the hosts file
For this, you will need to modify your *hosts* file. To do so, run `nano /etc/hosts` as root/with sudo.

When you've got it open, paste the following at the bottom:

```
163.172.71.251 osu.ppy.sh a.ppy.sh b.ppy.sh c.ppy.sh c1.ppy.sh s.ppy.sh
51.255.90.169 bm6.ppy.sh
```
**CTRL+X** and then **Enter** to save the file.

### Installing the certificate
Download the certificate by clicking [*here*](https://git.zxq.co/ripple/ripple-server-switcher/raw/master/RippleServerSwitcher/Resources/certificate.cer)

Open the Internet Explorer configuration by running `wine control`.

Double click the *Internet Settings* icon, navigate to the *Content* tab, then click the *Certificates...* button.

Click on *Import*, then *Next*.

Click *Browse...* then select the Ripple certificate.

Click *Next*.

Select *Place all certificates in the following store*, and click *Browse*.

Select **Trusted Root Certification Authorities**, and click *Ok*.

Click *Next*, *Finish*.

You should get a message saying **The import was successful**.


After that is done, you can start the client up, and log in with your Ripple credentials.