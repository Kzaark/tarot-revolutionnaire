#!/bin/bash

set -e

REPO="https://github.com/Kzaark/tarot-revolutionnaire.git"
INSTALL_DIR="/usr/local/share/rtarot"
BIN_DIR="/usr/local/bin"

echo "Installation de rtarot..."

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "Dépôt existant détecté, mise à jour..."
    git -C "$INSTALL_DIR" pull
else
    echo "Clonage du dépôt..."
    git clone "$REPO" "$INSTALL_DIR"
fi

cat > "$BIN_DIR/rtarot" << 'SCRIPT'
#!/bin/bash
python3 /usr/local/share/rtarot/rtarot.py "$@"
SCRIPT

chmod +x "$BIN_DIR/rtarot"
echo "✓ rtarot installé avec succès !"
echo "  Lance : rtarot"
