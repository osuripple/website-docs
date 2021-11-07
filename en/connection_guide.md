---
title: "How to connect to Ripple"
old_id: 1
---
- First, you have to [Register](http://ripple.moe/index.php?p=3) an account  


### How to play on Ripple (Windows Shortcut)
- **Create a shortcut** of your osu!.exe:
    - **If you already have an osu! shortcut on your desktop**, create a copy of it and rename it to "Ripple"
    - **If you don't have one:**
        - Find osu! in your start menu and click "Open file location"
        - Right click osu! in the file explorer and select Open file location
        - Hold Alt and drag osu! on your desktop
        - Click "Create shortcut here"

- Right click on the newly created shortcut and choose "Properties"
- Add a space and `-devserver ripple.moe` at the very end of the **"Target"** field
- **Open the "Ripple" shortcut** and enter your credentials to log in to Ripple

- A video tutorial on how to do this [is linked here](https://www.youtube.com/watch?v=NkDMdyLgF0U) 

### How to play on Ripple (Steam Shortcut)
- Add osu! as a non-Steam game on Steam
- Right click on osu! on Steam and select Properties
- Rename the game to "Ripple" and add a space and `-devserver ripple.moe` at the end of the "target" field

### How to play on Ripple (Linux)
- Open the script you use to launch osu
- Add `"$@"` after `osu!.exe` if it's not already present. So if it looks like this:

    ```sh
    wine osu\!.exe
    ```

    It will become

    ```sh
    wine osu\!.exe "$@"
    ```

- Then, add `-devserver ripple.moe` when you launch the script. So if you launch osu! with:

    ```sh
    ./osu.sh
    ```

    You can launch ripple with

    ```sh
    ./osu.sh -devserver ripple.moe
    ```

If you only play on ripple, you can also replace `"$@"` with `-devserver ripple.moe` so you don't have to type the server address each time

### How to play on official osu! again
You can simply launch the appropriate shortcut to launch either osu! or ripple.

Please note that, for security reasons, the client will log you out each time you switch servers.

### Having troubles?
You can check out out [Legacy connection guide](https://ripple.moe/doc/legacy_connection_guide) to use the server switched and https certificate to connect, however this method will be discontinued soon.

Also remember to check out our [FAQ](https://ripple.moe/doc/5)