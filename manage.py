#!/usr/bin/env python
import os.path
import re
import sys
from glob import glob
from pathlib import Path
from textwrap import dedent

import click
from ocdsextensionregistry import build_profile

basedir = Path(__file__).resolve().parent
sys.path.append(str(basedir / 'docs'))


@click.group()
def cli():
    pass


@cli.command()
def update():
    """
    Update the profile to the latest versions of extensions. If conf.py sets managed_codelist to True, regenerate
    docs/reference/codelists.md to list all codelists from OCDS and extensions.
    """

    import conf

    path_prefix = conf.html_theme_options['root_url']
    ref = conf.release.replace('-', '__').replace('.', '__')
    schema_base_url = f'https://standard.open-contracting.org{path_prefix}/schema/{ref}/'
    build_profile(basedir / 'schema', conf.standard_tag, conf.extension_versions, schema_base_url=schema_base_url)

    if not getattr(conf, 'managed_codelist', False):
        return

    file = basedir / 'docs' / 'reference' / 'codelists.md'
    with file.open('w+') as f:
        filenames = glob(str(basedir / 'schema' / 'patched' / 'codelists' / '*.csv'))
        codelists = [os.path.basename(filename) for filename in filenames]

        f.write(dedent(f"""\
        # Codelists

        <!-- Do not edit this file. This file is managed by manage.py -->

        For more information on codelists, refer to the [codelists reference](https://standard.open-contracting.org/1.1/en/schema/codelists/) in the OCDS documentation.

        The codelists below are from the OCDS and its extensions, and are provided here for convenience only.

        The codelists can be downloaded as CSV files from <https://standard.open-contracting.org/profiles/{conf.profile_identifier}/latest/en/_static/patched/codelists/>.
        """))  # noqa: E501

        for filename in sorted(codelists):
            heading = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', filename.replace('.csv', '')).title()

            f.write(f'\n## {heading}\n\n')

            f.write(dedent(f"""\
            ```{{csv-table-no-translate}}
            :header-rows: 1
            :class: codelist-table
            :file: ../_static/patched/codelists/{filename}
            ```
            """))


if __name__ == '__main__':
    cli()
