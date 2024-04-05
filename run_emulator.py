from desmume.emulator import DeSmuME
import os

emu = DeSmuME()
emu.open('emu/pw-aa.nds')

window = emu.create_sdl_window()
i = 0
while not window.has_quit():
    window.process_input()
    emu.cycle()
    window.draw()
    i+=1
    if i%1000 == 0:
        screenshot = emu.screenshot()
        screenshot.save(f'screenshots/screenshot_{emu.get_ticks()}.png')

