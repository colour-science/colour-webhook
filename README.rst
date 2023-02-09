Colour - Webhook
================

Introduction
------------

Various `webhook <https://github.com/adnanh/webhook>`__ resources for use with
`colour-science.org <https://github.com/colour-science/colour-science.org>`__.

Installation
------------

Pull
~~~~

.. code-block:: bash

    $ docker pull colourscience/colour-webhook

Run
~~~

.. code-block:: bash

    $ docker run -d --restart always \
    --name=colour-webhook \
    -e GITHUB_WEBHOOK_SECRET=$GITHUB_WEBHOOK_SECRET \
    -p 9010:9000 \
    -v /hooks:/etc/colour-webhook/hooks \
    -v /commands:/etc/colour-webhook/commands \
    -v /colour-science.org:/mnt/colour-science.org \
    colourscience/colour-webhook:latest \
    -verbose \
    -hotreload \
    -hooks=/etc/colour-webhook/hooks/hooks.json

Development
-----------

.. code-block:: bash

    $ conda create -y -n python-colour-webhook
    $ source activate python-colour-webhook
    $ conda install -y -c conda-forge colour-science
    $ conda install invoke requests

Code of Conduct
---------------

The *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,
is available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct/>`__ page.

Contact & Social
----------------

The *Colour Developers* can be reached via different means:

- `Email <mailto:colour-developers@colour-science.org>`__
- `Facebook <https://www.facebook.com/python.colour.science>`__
- `Gitter <https://gitter.im/colour-science/colour>`__
- `Twitter <https://twitter.com/colour_science>`__

About
-----

| **Colour - Webhook** by Colour Developers
| Copyright 2018 – Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__
| This software is released under terms of New BSD License: https://opensource.org/licenses/BSD-3-Clause
| `https://github.com/colour-science/colour-webhook <https://github.com/colour-science/colour-webhook>`__
