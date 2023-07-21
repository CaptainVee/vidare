
from django import template
from django.utils.html import escape, linebreaks

register = template.Library()

@register.filter
def paragraphs(value):
    """Converts newline characters to <p> tags."""
    paragraphs = [f"<p>{escape(p.strip())}</p>" for p in value.split('\n') if p.strip()]
    return "".join(paragraphs)

