"""This module provides the RP To-Do CLI."""
# analyser/cli.py

from typing import Optional

import typer

from analyser import __app_name__, __version__
from analyser.utils.helpers import check_address_reuse, common_inputs

app = typer.Typer()

@app.command()
def check_addr_reuse(psbt:str) -> None:
    """Check for address reuse in a PSBT."""
    result = check_address_reuse(psbt)
    if result["status"]:
       typer.secho(
            f"""
            {result["message"]}
            Inputs: {result["inputs"]}
            Outputs: {result["outputs"]}

            """,
            fg=typer.colors.RED,
        )
    elif result.get("inputs") and result.get("outputs"):
        typer.secho(
            f"""
            {result["message"]}
            Inputs: {result["inputs"]}
            Outputs: {result["outputs"]}
            """,
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""
            {result["message"]}
            """,
            fg=typer.colors.RED,
        )


@app.command()
def check_common_inputs(psbt:str) -> None:
    """Check for common inputs in a PSBT."""
    result = common_inputs(psbt)
    if result["status"]:
       typer.secho(
            f"""
            {result["message"]}
            Inputs: {result["inputs"]}
            Outputs: {result["outputs"]}

            """,
            fg=typer.colors.RED,
        )
    elif result.get("inputs") and result.get("outputs"):
        typer.secho(
            f"""
            {result["message"]}
            Inputs: {result["inputs"]}
            Outputs: {result["outputs"]}
            """,
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"""
            {result["message"]}
            """,
            fg=typer.colors.RED,
        )

@app.command()
def check_privacy(psbt:str) -> None:
    """Check for privacy issues in a PSBT."""
    result  = {"address_reuse": check_address_reuse(psbt)["status"], "common_inputs": common_inputs(psbt)["status"]}
    typer.secho(
            f"""
            {result}
            """,
            fg=typer.colors.GREEN,
        )



def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return