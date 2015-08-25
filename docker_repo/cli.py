#!/usr/bin/env python
from __future__ import print_function
import click
import os
import sys


# Based on the multi level CLI example from:
# https://github.com/mitsuhiko/click/tree/master/examples/complex
class ComplexCLI(click.MultiCommand):
    """Handles loading pluggable command files
    files must be in the commands path and start with cmd_"""

    def list_commands(self, ctx):
        cmd_list = []
        cmd_folder = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'commands'))
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_') and \
               'example' not in filename:
                cmd_list.append(filename[4:-3])
        cmd_list.sort()
        return cmd_list

    def get_command(self, ctx, name):
        ctx.command_name = name
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('docker_repo.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError as e:
            print('ERROR: Failed to import {}'.format(name))
            print(e)
        return mod.cli


@click.command(cls=ComplexCLI)
@click.help_option('--help', '-h')
@click.version_option(
    None, '--version', '-V',
    prog_name='docker_repo')
@click.option('--verbose', '-v', is_flag=True,
              help='Verbose output')
def cli(verbose):
    """
    docker_repo
    """
    # This will always run for every command so any
    # setup/teardown/sanity checking should go here
    # click.echo('CLI Hello')
    if verbose:
        click.echo("Running docker_repo")
