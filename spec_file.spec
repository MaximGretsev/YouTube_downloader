# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['/Users/user/Documents/Python/YouTube/main.py'],  # путь к main.py
             binaries=[],
             datas=[('merge.py', '.')],  # добавляем merge.py как data-файл
             hiddenimports=['pytube', 'moviepy', 'moviepy.video.io.VideoFileClip', 'moviepy.audio.io.AudioFileClip'],  # модули, которые нужны PyInstaller, но он не может определить их автоматически
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VideoMerger',  # имя выходного файла
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_include=[],
          runtime_tmpdir=None,
          console=True )  # выберите False, если вы хотите скрыть консольное окно
