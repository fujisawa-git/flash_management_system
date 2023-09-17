import pathlib
import time
import PySimpleGUI as sg

spell_info = [['teleport', 360, '../Spell_image/teleport.png'],
              ['flash', 300, '../Spell_image/flash.png']
]
def get_spellinfo(spell_name, kind):
    """サモナースペルの情報を引き出す関数"""
    """if とfor で多次元配列からタイマーを返す!"""
    return spell_info[kind][1]

layout = [[sg.Text('サモナースペル')],
          [sg.Combo(values=['teleport', 'flash'], size=(20, 1), key='SPELL', enable_events=True)]
          [sg.Text('タイマー')],
          [sg.Text(get_spellinfo(values['SPELL'], 1))],
]