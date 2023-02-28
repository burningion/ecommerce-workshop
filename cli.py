import click

@click.command()
@click.option('--version', prompt=True)
def choose_version(version):
    print(f"verion is {version}")

if __name__ == '__main__':
    choose_version()