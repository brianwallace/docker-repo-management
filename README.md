# docker-repo-management

A Python project for managing private docker repositories.

## Contributing

This utility uses the [Click][click] library for Python. If you're wondering why instead of optparse/argparse/etc it turns out that question is [already answered][click_why].

The subcommands are pluggable and located in the commands directory. Just name your file `cmd_[name_of_command].py` and take a look at the [cmd_example.py](atc/commands/cmd_example.py):

To easily iterate on the tool in development use `--editable`

`pip install --editable .`

## Todo

- Implement logic to [remove orphaned images](https://gist.github.com/kwk/c5443f2a1abcf0eb1eaa)
- Add logging
- Add tests


[click]: http://click.pocoo.org/3/
[click_why]: http://click.pocoo.org/3/why/
