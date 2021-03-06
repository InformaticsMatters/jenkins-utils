Informatics Matters Jenkins Utilities
=====================================

.. image:: https://github.com/InformaticsMatters/jenkins-utils/workflows/lint/badge.svg
   :target: https://travis-ci.com/InformaticsMatters/jenkins-utils

.. image:: https://badge.fury.io/py/im-jenkins-utils.svg
   :target: https://badge.fury.io/py/im-jenkins-utils

The ``im-jenkins-utils`` module is a set of utilities employed by
`Informatics Matters`_ for automated configuration of the Jenkins CI/CD
platform. It is a small library that currently simplifies the creation of Jobs,
secrets and other actions using `python-jenkins`_ and cURL.

It also includes a growing list of convenient wrapper functions to simplify
a number of tasks, like checking whether any jobs have failed
(or are unstable).

Typical use of the utilities relies on creating an ``ImJenkinsServer`` object
by providing a suitably formatted URL::

    from im_jenkins_server import ImJenkinsServer
    j_server = ImJenkinsServer(url)

The ``url`` value is typically of the form ``https://<user>:<token>@<url>``.

With this object you can then create a global text secret::

    if j_server.is_connected():
        j_server.set_secret_text('mySecretId', 'The Secret Text')

``ImJenkinsServer`` provides the following methods: -

* set_secret_text()
* set_secret_file()
* set_secret_user()
* get_jobs()
* set_jobs()
* get_views()
* set_views()
* check_jobs()

Configuration
-------------

You can provide configuration in a Python ConfigParser-style file.

At the moment this is used to provide a list of Jenkins Jobs that are excluded
during the ``check_jobs()`` method. If there are Jobs that can fail, that
you're not interested in, then you can provide their names via a configuration
file.

To exclude Jobs **Build (Experiment)** and **Run (Experiment)** you can provide
their names in the ``check`` *section* using the ``exclude-job`` *key*::

    [check]
    exclude-job: Build (Experiment)
        Run (Experiment)

And then pass the name and path of the configuration file to the server
object::

    j_server = ImJenkinsServer(url, 'config.ini')

Jobs are assumed to be tolerant of case and the Job names are checked
while ignoring the name case.

.. _Informatics Matters: http://www.informaticsmatters.com
.. _python-jenkins: https://pypi.org/project/python-jenkins
