"""Utilities for loading and rendering project templates."""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = Path(__file__).parent / "templates"

_env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)


def render_templates(destination: Path, **context) -> None:
    """Render all templates into the destination directory."""
    for template_path in TEMPLATES_DIR.rglob('*'):
        if template_path.is_dir():
            continue
        relative = template_path.relative_to(TEMPLATES_DIR)
        dest = destination / relative
        # strip .j2 suffix
        if dest.suffix == '.j2':
            dest = dest.with_suffix('')
        dest.parent.mkdir(parents=True, exist_ok=True)
        template = _env.get_template(str(relative))
        dest.write_text(template.render(**context))
