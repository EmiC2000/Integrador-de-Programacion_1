import pygame.mixer as mixer
import pygame as pg

music_configs = {
    "actual_music_path": ''
}

def set_music_path(music_path: str):
    """funcion el cual lleva a cabo set music path.

    Args:
        music_path (tipo): descripcion del parametro music_path.

    """
    music_configs['actual_music_path'] = music_path

def play_music():
    """funcion el cual lleva a cabo play music.

    """
    if music_configs.get('actual_music_path'):

        mixer.music.load(music_configs.get('actual_music_path'))

        mixer.music.play(-1, 0, 2500)

def get_actual_volume() -> int:
    """funcion el cual lleva a cabo get actual volume.

    Returns:
        tipo: descripcion del valor devuelto.

    """
    actual_vol = mixer.music.get_volume() * 100
    return int(actual_vol)

def set_volume(volume: int):
    """funcion el cual lleva a cabo set volume.

    Args:
        volume (tipo): descripcion del parametro volume.

    """
    actual_vol = volume / 100
    actual_vol = round(actual_vol, 1)
    mixer.music.set_volume(actual_vol)

def stop_music():
    """funcion el cual lleva a cabo stop music.

    """
    if music_configs.get('actual_music_path'):
        mixer.music.fadeout(500)
        pg.time.wait(500)
        mixer.music.stop()
