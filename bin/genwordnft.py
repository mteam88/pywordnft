#!/usr/bin/env python

from email.policy import default
import click, json, os

from pywordnft.genimage import Image

@click.command()
@click.argument('json-path', type=click.Path(exists=True))
@click.argument('results-dir', type=click.Path(dir_okay=True, file_okay=False))
@click.option('--output-fileext', default='jpeg')
def drawimagesfromjson(json_path, results_dir, output_fileext='jpeg'):
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    for image in Image.loadfromjson(json_path):
        image.draw().save(f'{os.path.abspath(results_dir)}/{image.title}.{output_fileext}')