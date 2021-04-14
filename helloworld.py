import click

@click.command()
@click.option('-c', '--case', type=click.Choice(['upper', 'lower']))
@click.argument('person', default='you')
def hello(case, person):
    response = "Hello World! Also, hey {} ☺️".format(person)
    if case == 'upper':
        click.echo(response.upper())
    elif case == 'lower':
        click.echo(response.lower())
    else:
        click.echo(response)

# if __name__ == '__main__':
#     hello()
