from desmume.emulator import DeSmuME

emu = DeSmuME()
emu.open('emu/pw-aa.nds')

window = emu.create_sdl_window()

while not window.has_quit():
    window.process_input()
    emu.cycle()
    window.draw()