# Sublime Text 2 plugin: Search CakePHP API

A command to search the CakePHP API for the current word.

## Supports

 * CakePHP 2.x

Submit a patch adding more and I'll include it.

## Using

Open the command palette (cmd-shift-p) and choose "Search CakePHP API" while your cursor is on a word.

Make a keybind by adding the following to your `User/Default (OSX).sublime-keymap`:

    { "keys": ["super+shift+a"], "command": "cakephpapi_search_selection" },
    { "keys": ["ctrl+shift+a"], "command": "cakephpapi_search_from_input" }

(I don't like plugins automatically adding keybinds, okay.)

## Installing

### With Package Control

The easiest way to install this package is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select "Search CakePHP API" when the list appears.

First, you need to have `git` installed and in your `$PATH`. Afterwards you may need to restart Sublime Text 2 before the plugin will work.

### Without Git

Download the latest source zip from [github](https://nodeload.github.com/jadb/st2-search-cakephp-api/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named Search CakePHP.

### With Git

### OSX

    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    $ git clone git://github.com/jadb/st2-search-cakephp-api.git "Search CakePHP API"

### Linux (Ubuntu like distros)

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone git://github.com/jadb/st2-search-cakephp-api.git "Search CakePHP API"

### Windows 7:

    Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages"

### Windows XP:

    Copy the directory to: "C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages"
