# -*- coding: utf-8 -*-
"""
Invoke - Tasks
==============
"""

from __future__ import print_function, unicode_literals

import hashlib
import hmac
import os
import requests
from invoke import task
from invoke.exceptions import Failure

from colour.utilities import message_box

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2018-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'APPLICATION_NAME', 'ORG', 'CONTAINER', 'clean', 'formatting',
    'docker_build', 'docker_remove', 'docker_run'
]

APPLICATION_NAME = 'Colour - Webhook'

ORG = 'colourscience'

VERSION = '0.1.0'

CONTAINER = APPLICATION_NAME.replace(' ', '').lower()


@task
def clean(ctx, bytecode=False):
    """
    Cleans the project.

    Parameters
    ----------
    bytecode : bool, optional
        Whether to clean the bytecode files, e.g. *.pyc* files.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Cleaning project...')

    patterns = []

    if bytecode:
        patterns.append('**/*.pyc')

    for pattern in patterns:
        ctx.run("rm -rf {}".format(pattern))


@task
def formatting(ctx, yapf=False):
    """
    Formats the codebase with *Yapf*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    yapf : bool, optional
        Whether to format the codebase with *Yapf*.

    Returns
    -------
    bool
        Task success.
    """

    if yapf:
        message_box('Formatting codebase with "Yapf"...')
        ctx.run('yapf -p -i -r .')


@task
def docker_build(ctx):
    """
    Builds the *docker* image.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Building "docker" image...')

    ctx.run('docker build -t {0}/{1}:latest -t {0}/{1}:v{2} .'.format(
        ORG, CONTAINER, VERSION))


@task
def docker_remove(ctx):
    """
    Stops and remove the *docker* container.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Stopping "docker" container...')
    try:
        ctx.run('docker stop {0}'.format(CONTAINER))
    except Failure:
        pass

    message_box('Removing "docker" container...')
    try:
        ctx.run('docker rm {0}'.format(CONTAINER))
    except Failure:
        pass


@task(docker_remove, docker_build)
def docker_run(ctx):
    """
    Runs the *docker* container.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Running "docker" container...')
    ctx.run('docker run -d '
            '--name={1} '
            '-e GITHUB_WEBHOOK_SECRET=$GITHUB_WEBHOOK_SECRET '
            '-p 9010:9000 '
            '-v {2}:/etc/colour-webhook/hooks '
            '-v {3}:/etc/colour-webhook/commands '
            '-v {4}:/mnt/colour-science.org '
            '{0}/{1} '
            '-verbose '
            '-hotreload '
            '-template '
            '-hooks=/etc/colour-webhook/hooks/hooks.json '.format(
                ORG, CONTAINER, os.path.abspath('hooks'),
                os.path.abspath('commands'),
                os.path.abspath(os.path.join('..', 'colour-science.org'))))


@task
def docker_push(ctx):
    """
    Pushes the *docker* container.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Pushing "docker" container...')
    ctx.run('docker push {0}/{1}'.format(ORG, CONTAINER))


@task
def emulate_github_webhook(ctx):
    """
    Emulates *Github* webhook.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    message_box('Emulating "Github" webhook...')
    github_webhook_secret = os.environ.get('GITHUB_WEBHOOK_SECRET')

    with open(os.path.join('resources', 'payload.json'), 'r') as payload_file:
        payload_content = payload_file.read()

    data = '{{"ref": "{0}"}}'.format(payload_content)
    digest = hmac.new(
        github_webhook_secret, data, digestmod=hashlib.sha1).hexdigest()

    headers = {'X-Hub-Signature': 'sha1={0}'.format(digest)}
    print(requests.post(
        'http://0.0.0.0:9010/hooks/colour-science.org',
        headers=headers,
        data=data).text)
