import click
import sys
import json
from docker_repo.dockerregistry import DockerRegistry


# @click.group creates a subcommand group
@click.group('remove')
# @pass_config passes in the config object from top level
# All your commands should get this object to handle things like verbose
# or other global options
@click.help_option('--help', '-h')
@click.option('--verbose', '-v', is_flag=True,
              help='Verbose output')
def cli(verbose):
    """
    Remove docker images
    """
    # This will be executed before your command
    if verbose:
        click.echo("remove")


@cli.command("repository")
@click.argument('repo', nargs=1)
@click.help_option('--help', '-h')
@click.option('--verbose', '-v', is_flag=True,
              help='Verbose output')
def repository(verbose, repo):
    """
    Remove a repository version
    """
    if verbose:
        click.echo("remove repository")

    registry = DockerRegistry("http://registry.airware.corp.msp/v1")

    # r = dr.get('/repositories/library/baldr/tags',
    #           headers={'Accept': 'application/json'})
    r = registry.get('/repositories/library/{}/tags'.format(repo))
    json_object = r.json()
    if r.status_code != 200:
        raise Exception("docker registry error {}".format(r.status_code))

    #images = ' '.join([value for key, value in json_object.items()])
    #print images
    images = []
    for tag in json_object.keys():

        r = registry.delete('/repositories/library/{}/tags/{}'.format(repo, tag))
        delete_obj = r.json()
        if r.status_code != 200:
            raise Exception("Error deleting tag {} from docker repository {}.  Status Code {}.".format(
                tag,
                repo,
                r.status_code))
            sys.exit(1)

        images.append(json_object[tag])

    print ' '.join(images)
