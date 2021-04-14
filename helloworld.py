import click

@click.command()
@click.option('-c', '--case', type=click.Choice(['upper', 'lower']))
def hello(case):
    response = "Hello World!"
    if case == 'upper':
        click.echo(response.upper())
    elif case == 'lower':
        click.echo(response.lower())
    else:
        click.echo(response)

# if __name__ == '__main__':
#     hello()
