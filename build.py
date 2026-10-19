"""Builds the self-contained pages served by GitHub Pages:
index.html (English, default) and fa.html (Persian), from src/deck.html + src/fonts.css."""
import sys
from pathlib import Path
root = Path(__file__).parent
sys.path.insert(0, str(root / 'src'))
from en import to_english

deck = (root / 'src/deck.html').read_text(encoding='utf-8')
fonts = (root / 'src/fonts.css').read_text(encoding='utf-8').strip()
fa = deck.replace('/*FONTS*/', fonts, 1)
(root / 'fa.html').write_text(fa, encoding='utf-8')
(root / 'index.html').write_text(to_english(fa), encoding='utf-8')
print('index.html (English) and fa.html (Persian) written')
