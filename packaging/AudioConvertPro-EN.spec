# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

REPO_ROOT = Path(SPECPATH).resolve().parent
SOURCE_DIR = REPO_ROOT / "src"
SOURCE_FILE = SOURCE_DIR / "AudioConvertPro_EN.py"
ICON_FILE = REPO_ROOT / "assets" / "icon.ico"

datas = [(str(ICON_FILE), ".")]
binaries = []
hiddenimports = ["tkinterdnd2", "ctypes", "_ctypes"]

for package in ("customtkinter", "tkinterdnd2", "PIL"):
    package_data, package_binaries, package_hiddenimports = collect_all(package)
    datas += package_data
    binaries += package_binaries
    hiddenimports += package_hiddenimports

a = Analysis(
    [str(SOURCE_FILE)],
    pathex=[str(SOURCE_DIR)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="AudioConvertPro",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(ICON_FILE),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="AudioConvertPro",
)
