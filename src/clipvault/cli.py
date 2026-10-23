#!/usr/bin/env python3
import click,json
from pathlib import Path
from rich.console import Console
console=Console()
STORE=Path.home()/'.clipvault.json'
@click.group()
def main(): pass
@main.command()
@click.argument('text')
def save(text):
    data=[]
    if STORE.exists(): data=json.loads(STORE.read_text())
    data.append(text)
    STORE.write_text(json.dumps(data))
    console.print('[green]Saved[/green]')
@main.command()
def list():
    if not STORE.exists(): console.print('Empty'); return
    for i,t in enumerate(json.loads(STORE.read_text())): console.print(f'{i}: {t}', markup=False)
if __name__=='__main__': main()
