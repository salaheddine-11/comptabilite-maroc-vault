# -*- coding: utf-8 -*-
"""Rasterize canvas_preview.svg to PNG via cairosvg."""
import cairosvg

cairosvg.svg2png(
    url=r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\98 Outils\canvas_preview.svg",
    write_to=r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\98 Outils\canvas_preview.png",
    scale=2.0,
)
print("PNG OK")
