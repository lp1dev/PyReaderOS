import sys
sys.path.append('/home/lp1/PyReaderOS')
import conf
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([], "XF86PowerOff", lazy.spawn("sudo /usr/bin/suspend.sh")),

    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile")
]

groups = [Group(i) for i in "12"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
#    layout.Max(),
    # Try more layouts by unleashing below layouts.
#    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar([], conf.BOTTOM_BAR_SIZE),
        top=bar.Bar([], conf.TOP_BAR_SIZE)
    ),
]

# Drag floating layouts.
mouse = [
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list

follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="!toplevel9"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry,
        Match(title="Onboard"),
        Match(title="Tab"),
        Match(wm_class="feh")
    ]
)

@hook.subscribe.client_urgent_hint_changed
def focus_urgent(c):
    logger.warn('in focus')
    logger.warn(c.name)
    c.cmd_focus()
    c.cmd_enable_fullscreen()

auto_fullscreen = False
focus_on_window_activation = "urgent"
floats_kept_above = True
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["/bin/sh", "/home/lp1/PyReaderOS/start.sh"])
