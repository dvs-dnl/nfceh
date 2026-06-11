#!/bin/bash
# Download original images from Wix into assets/ BEFORE cancelling the Wix plan.
# Run from the site root:  bash download-assets.sh
set -e
cd "$(dirname "$0")"
W="https://static.wixstatic.com/media"
dl() { echo "-> $2"; curl -fsSL "$1" -o "$2" || echo "   FAILED: $1"; }

dl "$W/7c19a7_ccd42cc13f054bff89f77256a0a99337~mv2.png"  assets/images/logo.png
dl "$W/7c19a7_ab4cb8f88528469ca0c851084d461f79~mv2.png"  assets/images/heart.png
dl "$W/baac51_037dbf236c3f4e948b88b0618ad53120~mv2.jpg"  assets/images/about-vertical.jpg
dl "$W/55d98a_aeec24ea4668401a88c440d765e6d22d~mv2.jpg"  assets/images/about-horizontal.jpg
dl "$W/7c19a7_0616d4b2ade649729d41ef1ee976b563~mv2.jpg"  assets/images/kevin-nye.jpg
dl "$W/7c19a7_c4116d41b21a4a489664d7170ffb37b4~mv2.png"  assets/images/aaron-horner.png
dl "$W/7c19a7_ce31a43620824304924fb78c1ef55354~mv2.jpeg" assets/images/rashida-tyler.jpeg
dl "$W/7c19a7_38ca28d1a0b94a388394399999a7904a~mv2.jpeg" assets/images/sparrow-etter-carlson.jpeg
dl "$W/7c19a7_461492d583cd41ec88aade436902be25~mv2.jpg"  assets/images/daniel-davis.jpg
dl "$W/ae63f0_155c6a4ee4434b828c7545e02925b67e~mv2.png"  assets/images/hs-hero.png
dl "$W/7c19a7_f42043825e76433daa6429e7575e48b4~mv2.png"  assets/images/mosaic-sphere.png
dl "$W/7c19a7_e11b0ec5987a437c8aa0f86585478272~mv2.png"  assets/images/blog-header.png
dl "https://www.nfceh.org/_files/ugd/ae63f0_0ddc68085bc44ee783fc8b78e2da70aa.pdf" assets/files/homelessness-sunday-flyer.pdf

# Favicon: a square crop of the logo works; replace with a real favicon when ready.
cp assets/images/logo.png assets/images/favicon.png
echo "Done. Review the images, then commit assets/ to the repo."
