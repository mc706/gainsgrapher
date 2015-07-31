#Fabric Commands

This repository uses a number of fabric commands. Here is a short list of what they are, 
how to use them, and what they do.

The Following Commands are designed for use.

* `cut`
* `vagrant`
* `freeze`
* `test`
* `quality_check`

###test

Run as `fab test` this command runs a number of different tests and conditions. It pulls the list of installed applications
from `gainsgrapher/installed_apps` and runs a full BehaveTestSuite and DjangoTestSuite against them with coverage. 

If both of the tests suites are complete, it runs a coverage check. If the coverage does not pass 100%, it fails.

If coverage is 100%, it then runs `quality_check` which is a `pep8` check against the repo, to make sure that all new
code is pep8 compliant.

Only when all of these tests pass does `fab test` return 0.

Configuration for the coverage is in `.coveragerc`.

###quality_check

Runs the `pep8` tests. Configuration for these is in `tox.ini`.

###cut

Run as `fab cut`, this commands takes 2 arguments. It takes `release`, which defaults to `patch`. 
Release has 4 options:

* major
* minor
* patch (Default)

Depending on which one you choose, it will bump the version number as a result of it. 
This Repository uses semantic style versioning (major.minor.patch). It will also automatically
update the `CHANGELOG.md` file with all the commit messages since your last cut version. If you call
`cut` without a release, it will default to `patch`.

The other option is `env`. This selects which environment fabric will deploy the change to.
The two options are:

* dev (default)
* prod

By default, it will deploy to dev. This will checkout the development branch in the appropriate folder
git pull, bower install, collectstatic, migrate, and restart the web server. 

The Notifications call uses `api_version` header which links to the `_version.py` version number. If the 
server's version is different than the one that the frontend was loaded with, it will show a notification
and prompt the user to restart.
 
This command will only execute if `fab test` passes and return as 0.

###vagrant
 
The vagrant command is a shortcut command to run vagrant commands and the ansible script from the root directory.

`fab vagrant:up`

`fab vagrant:provision`

`fab vagrant:halt`
 
###freeze

This shortcut command pipes pip requirements into requirements.txt

```
pip freeze > requirements.txt
```