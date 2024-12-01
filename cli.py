import subprocess
import click
import shutil

@click.group()
@click.option('--arch', type=click.Choice(['x86_64', 'arm64']), default='x86_64')
@click.pass_context
def cli(ctx, arch):
    ctx.ensure_object(dict)
    ctx.obj['ARCH'] = arch
    click.echo(f"Building for {arch}")

@cli.command()
@click.pass_context
def build(ctx):
    arch = ctx.obj['ARCH']
    build_command = [
        "pdm", "run", "nuitka", "nuitka_3224.py",
        "--standalone",
        "--macos-create-app-bundle",
        f"--macos-target-arch={arch}",
        f"--output-dir={arch}",
    ]
    subprocess.run(build_command)

@cli.command()
@click.pass_context
def dmg(ctx):
    arch = ctx.obj['ARCH']
    create_dmg_command = [
        "create-dmg",
        "--volname", "nuitka-3224",
        "--window-size", "500", "300",
        "--icon-size", "100",
        "--icon", "nuitka_3224.app", "100", "150",
        "--hide-extension", "nuitka_3224.app",
        "--app-drop-link", "100", "185",
        f"nuitka_3224-{arch}.dmg",
        f"{arch}/nuitka_3224.app",
    ]
    subprocess.run(create_dmg_command)
    shutil.copy(f"nuitka_3224-{arch}.dmg", f"dist/nuitka_3224-{arch}.dmg")

if __name__ == '__main__':
    cli(obj={})
