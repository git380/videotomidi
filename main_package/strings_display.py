# window
color_window_title = 'color map'
settings_window_title = 'Settings'
help_window_title = 'help'
extra_window_title = 'extra/experimental'
sparks_window_title = 'sparks & color settings'

# label
help_label = '''h - on window title, show/hide the window
q - begin to recreate midi
s - set start frame, (mods : shift, set processing start frame to the beginning)
e - set end frame, (mods : shift, set processing end frame to the ending)
p - if key is set, force separate to 2 channels (on single color video)
o - enable or disable overlap notes
i - enable or disable ignore/lengthening of notes with minimal duration
r - enable or disable resize function
Mouse wheel - keys adjustment
Left mouse button - dragging the selected key / select color from the color map
CTRL + Left mouse button - update selected color in the color map
CTRL + 0 - disable selected color in the color map
Right mouse button - dragging all keys, if the key is selected, the transfer is carried out relative to it.
Arrows - keys adjustment (mods : shift) ( Atl+Arrows UP/Down - sparks position adjustment )
+(PLUS) / - (MINUS) - rotate keys by 5*
PageUp/PageDown - scrolling video (mods : shift)
Home/End - go to the beginning or end of the video
[ / ] - change base octave
F2 / F3 - save / load settings, F4 - move all windows to the mouse point
Escape - quit, TAB - Show/Hide all windows
Space - abort re-creation and save midi file to disk'''

# extra/experimental
use_alternate_label = 'Use alternate:'
selected_key_sensitivity_label = 'Selected key sensitivity'
select_deselect_key_label = '''to select the key press ctrl + left mouse button on the key rect.
to deselect the key press ctrl + left mouse button on empty space.'''

# sparks & color settings
move_sparks_label = 'alt + up / down - move sparks label up or down '

# Button Labels
# Settings Button Labels
start_recreate_midi_label = 'start recreate midi'
set_start_frame_label = 'set start frame'
set_end_frame_label = 'set end frame'
notes_overlap_label = 'notes overlap'
ignore_notes_with_minimal_duration_label = 'ignore notes with minimal duration'
sync_notes_label = 'sync notes'
resize_window_label = 'resize window'
auto_close_label = 'auto-close'
save_settings_label = 'save settings'
load_settings_label = 'load settings'
roll_check_label = 'roll check'
per_channel_save_label = 'per channel save'
rollcheck_white_keys_priority_label = 'rollcheck white keys priority'

# color map Button Labels
read_colors_label = 'read colors'
update_color_label = 'update color'
enable_disable_label = 'enable/disable'
snap_notes_to_grid_label = 'snap notes to grid'

# sparks & color settings Button Labels
use_sparks_label = 'use sparks'
use_percolor_sensitivity_label = 'use percolor sensitivity'

# Settings Labels
base_octave_label = 'base octave: '

# Slider Labels
# Settings Slider Labels
sensitivity_label = 'Sensitivity'
minimal_note_duration_label = 'Minimal note duration (sec)'
output_tempo_for_midi_label = 'Output tempo for midi'
output_midi_format_label = 'Output midi format'
black_key_relative_pos_label = 'black key relative pos'
sync_notes_time_delta_label = 'sync notes time delta (ms)'

# color map Slider Labels
sparks_delta_label = 'Sparks delta'

# sparks & color settings Slider Labels
line_height_label = 'Length of Vertical Key Lines'
sparks_height_label = 'Sparks height'
percolor_sensitivity_label = 'percolor sensitivity'


# hint Labels
# Settings hint Labels
hint_start_recreate_midi = 'q - hot key'
hint_set_start_frame = 's - hot key, (mods : shift + s, set processing start frame to the beginning)'
hint_set_end_frame = 'e - hot key, (mods : shift + e, set processing end frame to the ending)'
hint_notes_overlap = 'o - hot key'
hint_ignore_notes_with_minimal_duration = 'i - hot key'
hint_sync_notes = 'sync notes start pos'
hint_resize_window = 'r - hot key'
hint_exit_switch = 'exit after the completion of the midi reconstruction'
hint_save_settings = 'F2 - hot key, save current settings'
hint_load_settings = 'F3 - hot key, load saved settings'
raise_octave_hint = '] - hot key, move up base octave (+12 tones)'
lower_octave_hint = '[ - hot key, move down base octave (-12 tones)'
per_channel_save_hint = 'split the output midi per channels'

# color map hint Labels
disable_color_hint = 'ctrl+0 - shortcut, disable selected color'

# sparks & color settings hint Labels
move_sparks_higher_hint = 'move sparks higher'
move_sparks_lower_hint = 'move sparks lower'


# navbtns_info
hint_home = 'Home - hot key, go to first frame'
hint_page_down = 'PageDown - hot key, fast scroll backward'
hint_shift_page_down = 'Shift+PageDown - shortcut, scroll backward by frame'
hint_shift_page_up = 'Shift+PageUp - shortcut, scroll forward by frame'
hint_page_up = 'PageUp - hot key, fast scroll forward'
hint_end = 'End - hot key, go to last frame'
hint_rotate_cw = 'rotate the keys clockwise, hot key +'
hint_rotate_ccw = 'rotate the keys counterclockwise, hot key -'
