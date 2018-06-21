Informatics Matters Jenkins Utilities
=====================================

The ``im-jenkins-utils`` module is a set of utilities employed by
`Informatics Matters`_ for automated configuration of the Jenkins CI/CD
platform. It is a small library that currently simplifies the creation of Jobs
using `python-jenkins`_ and various credential types using cURL.

Typical use of the utilities relies on creating an ``ImJenkinsServer`` class
by providing a suitably formatted URL::

    from im_jenkins_server import ImJenkinsServer
    j_server = ImJenkinsServer(url)

The ``url`` value is typically of the form ``https://<user>:<token>@<url>``.

With this class you can then create a global text secret::

    j_server.set_secret_text('mySecretId', 'The Secret Text')

The server following methods exist: -

* set_secret_text()
* set_secret_file()
* set_secret_user()
* get_jobs()
* set_jobs()

.. _Informatics Matters: http://www.informaticsmatters.com
.. _python-jenkins: https://pypi.org/project/python-jenkins