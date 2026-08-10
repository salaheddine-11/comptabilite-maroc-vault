#!/bin/bash
# Batch-download AMMC documents de référence (exercice 2025) into the vault.
set -u
VAULT_DOCS="/c/Users/salah eddine/Desktop/Reasearch/Reasearch/96 Documents Réels"
mkdir -p "$VAULT_DOCS/01 Documents de référence AMMC"
cd "$VAULT_DOCS/01 Documents de référence AMMC" || exit 1
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

LIST=$(curl -s --max-time 40 "https://www.ammc.ma/fr/espace-emetteurs/enregistrements" -A "$UA" \
  | grep -oP 'href="/fr/espace-emetteurs/documents-enregistres/[^"]+"' \
  | sed 's/href="//; s/"$//' | sort -u)

for slug in $LIST; do
  name=$(echo "$slug" | sed 's|/fr/espace-emetteurs/documents-enregistres/||' | cut -c1-45)
  [ -f "${name}.pdf" ] && [ "$(stat -c%s "${name}.pdf")" -gt 100000 ] && { echo "SKIP (exists): ${name}"; continue; }
  page="https://www.ammc.ma${slug}"
  pdf=$(curl -s --max-time 30 "$page" -A "$UA" \
        | grep -oP '(?:https://www\.ammc\.ma)?/sites/default/files/[^"]*\.pdf' | head -1)
  if [ -n "$pdf" ]; then
    case "$pdf" in
      http*) full="$pdf" ;;
      *) full="https://www.ammc.ma${pdf}" ;;
    esac
    curl -sL --max-time 180 -A "$UA" -o "${name}.pdf" "$full"
    sz=$(stat -c%s "${name}.pdf" 2>/dev/null || echo 0)
    echo "${name}.pdf | ${sz} octets | $(head -c 4 "${name}.pdf" 2>/dev/null | od -An -c | tr -d ' \n')"
  else
    echo "NO PDF on: ${name}"
  fi
  sleep 1
done
echo "ALLDONE"
