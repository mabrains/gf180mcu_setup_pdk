#!/bin/bash

# =========================================================================================
# Copyright 2025 Mabrains Company
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================================

# Exit on error
set -e

# Check if PDK_ROOT is set
if [ -z "$PDK_ROOT" ]; then
  echo "❌ Error: PDK_ROOT is not set. Please export it before running this script."
  echo "   Example: export PDK_ROOT=\$HOME/pdks"
  exit 1
fi

PDK_ROOT=$(realpath "$PDK_ROOT")

# Set default values
PDK="gf180mcu"

# Check for ciel
if ! command -v ciel &> /dev/null; then
  echo "📦 Installing ciel..."
  python3 -m pip install --user --upgrade ciel
fi

# Confirm ciel is installed
if ! command -v ciel &> /dev/null; then
  echo "❌ ciel installation failed or not in PATH"
  exit 1
fi

echo "🔍 Fetching latest hash for $PDK..."
LATEST_HASH=$(ciel ls-remote --pdk-family "$PDK" | awk 'NR==2 {print $1}')

if [ -z "$LATEST_HASH" ]; then
  echo "❌ Could not get latest hash for $PDK"
  exit 1
fi

echo "📥 Enabling $PDK ($LATEST_HASH)..."
ciel enable --pdk-family "$PDK" "$LATEST_HASH"
