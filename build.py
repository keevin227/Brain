"""Builds the self-contained index.html (served by GitHub Pages) from src/deck.html + src/fonts.css."""
from pathlib import Path
root = Path(__file__).parent
deck = (root / 'src/deck.html').read_text(encoding='utf-8')
fonts = (root / 'src/fonts.css').read_text(encoding='utf-8').strip()
(root / 'index.html').write_text(deck.replace('/*FONTS*/', fonts, 1), encoding='utf-8')
print('index.html written')
