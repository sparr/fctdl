
FCTDL
-----

download factorio comfortably from your command line::

    $ fctdl -a x86 0.13.2 ./
    username: my_username
    password:

you can also store login data in a yaml file::

    $ cat ~/.config/fctdl.yml
    username: foobar
    password: secret

to avoid re-entering that information.
Listing available versions is possible with::

    $ fctdl list experimental
    INFO:fctdl.factorio:logging in.
    INFO:fctdl.factorio:requesting versions.
    * 0.14.8 (alpha)
    * 0.14.8 (headless)
    * 0.14.7 (alpha)
    * 0.14.7 (headless)
    * 0.14.6 (alpha)
    * 0.14.6 (headless)
    * 0.14.5 (alpha)
    * 0.14.5 (headless)
    * 0.14.4 (alpha)
    * 0.14.4 (headless)
    * 0.14.3 (alpha)
    * 0.14.3 (headless)
    * 0.14.2 (alpha)
    * 0.14.2 (headless)
    * 0.14.1 (alpha)
    * 0.14.1 (headless)
    * 0.14.0 (alpha)
    * 0.14.0 (headless)


