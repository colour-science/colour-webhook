Colour - Webhook
================

Introduction
------------

Various `webhook <https://github.com/adnanh/webhook>`_ resources for use with
`colour-science.org <https://github.com/colour-science/colour-science.org>`_.

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

About
-----

| **Colour - Webhook** by Colour Developers
| Copyright © 2018 – Colour Developers – `colour-science@googlegroups.com <colour-science@googlegroups.com>`_
| This software is released under terms of New BSD License: http://opensource.org/licenses/BSD-3-Clause
| `http://github.com/colour-science/colour-webhook <http://github.com/colour-science/colour-webhook>`_
