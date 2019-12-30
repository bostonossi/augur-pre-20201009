<<<<<<< Updated upstream
import click
=======
#SPDX-License-Identifier: MIT
"""
Miscellaneous Augur library commands for controlling the backend components
"""

>>>>>>> Stashed changes
import os
import subprocess
import click

from augur.runtime import pass_application

@click.group('util', short_help='Miscellaneous utilities')
def cli():
    pass

@cli.command('shell', short_help='Drop into a shell')
@pass_application
def shell(app):
    app.shell()

@cli.command('kill', short_help='Kill Augur')
@pass_application
def kill(app):
    """
    kill running augur processes
    """
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    subprocess.call("../../util/scripts/control/augurkill.sh")

@cli.command('repo-reset', short_help='Reset Repo Collection')
@pass_application
def kill(app):
    """
    kill running augur processes
    """
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    subprocess.call('../../util/scripts/control/repo-reset.sh')
