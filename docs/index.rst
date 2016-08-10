====================
myprj.theme
====================

$ cd ~/Plone/zinstance/src
$ ../bin/mrbob -O myprj.theme bobtemplates:plone_addon

Welcome to mr.bob interactive mode. Before we generate directory structure, some questions need to be answered.

Answer with a question mark to display help.
Values in square brackets at the end of the questions show the default value if there is no answer.


--> What kind of package would you like to create? Choose between 'Basic', 'Dexterity', and 'Theme'. [Basic]: Theme

--> Author's name [TsungWei Hu]:

--> Author's email [marr.tw@gmail.com]:

--> Author's github username: l34marr

--> Package description [An add-on for Plone]:

--> Plone version [4.3.9]:


Generated file structure at /home/marr/Plone/zinstance/src/myprj.theme


$ cd ~/Plone/zinstance
$ bin/buildout -c develop.cfg
mr.developer: Queued 'myprj.theme' for checkout.
mr.developer: Filesystem package 'myprj.theme' doesn't need a checkout.
Develop: '/home/marr/Plone/zinstance/src/myprj.theme'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
Updating _mr.developer.
Updating instance.
Generated script '/home/marr/Plone/zinstance/bin/instance'.
Generated interpreter '/home/marr/Plone/zinstance/parts/instance/bin/interpreter'.
Generated script '/home/marr/Plone/zinstance/bin/pilprint.py'.
Generated script '/home/marr/Plone/zinstance/bin/createfontdatachunk.py'.
Generated script '/home/marr/Plone/zinstance/bin/pilfont.py'.
Generated script '/home/marr/Plone/zinstance/bin/pilfile.py'.
Generated script '/home/marr/Plone/zinstance/bin/pildriver.py'.
Generated script '/home/marr/Plone/zinstance/bin/player.py'.
Generated script '/home/marr/Plone/zinstance/bin/thresholder.py'.
Generated script '/home/marr/Plone/zinstance/bin/explode.py'.
Generated script '/home/marr/Plone/zinstance/bin/painter.py'.
Generated script '/home/marr/Plone/zinstance/bin/enhancer.py'.
Generated script '/home/marr/Plone/zinstance/bin/gifmaker.py'.
Generated script '/home/marr/Plone/zinstance/bin/viewer.py'.
Generated script '/home/marr/Plone/zinstance/bin/pilconvert.py'.
Updating repozo.
Updating backup.
Updating zopepy.
Generated interpreter '/home/marr/Plone/zinstance/bin/zopepy'.
Updating unifiedinstaller.
Updating test.
Generated script '/home/marr/Plone/zinstance/bin/test'.
Updating diazotools.
Updating checkdocs.
Updating mrbob.
Updating releaser.

