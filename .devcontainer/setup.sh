# !/bin/bash

set -e

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

. ~/.bashrc

pip3 install esbonio>=0.12.0

sudo apt update && sudo apt install -y \
  texlive-latex-recommended \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-latex-extra \
  latexmk \
  texlive-xetex \
  fonts-freefont-otf
