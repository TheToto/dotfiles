from i3pystatus import Status
from i3pystatus.calendar.lightning import Lightning

from addons.backlight_custom import BacklightCustom
from addons.network_custom import NetworkCustom
from addons.redshift_manual import RedshiftManual
from addons.rfkill import Rfkill
from addons.xautolock import Xautolock

status = Status()

status.register(Rfkill, format="", rfkill_override_command_name="bluetooth",
                rfkill_name="tpacpi_bluetooth_sw", on_middleclick="rofi-bluetooth")
status.register(Rfkill, format="", rfkill_name="phy0")

status.register(Xautolock)

status.register("mpd", format="{status}", status={"pause": "", "play": "", "stop": ""},
                on_middleclick=["mpd_command", "shuffle"],
                on_rightclick=["mpd_command", "stop"],
                on_doubleleftclick="rofi-mpd")

status.register("clock", format=" %d/%m  %X", interval=1)

calendar_path = "/home/toto/.thunderbird/qv47hklh.default-release/calendar-data/cache.sqlite"
status.register("calendar",
                format="{title:10.10} {humanize_remaining}",
                interval=60,
                urgent_blink=True,
                backend=Lightning(database_path=calendar_path, days=7))

status.register("cpu_usage", format="  {usage:\u2002>2}%", interval=5)

status.register(
    "battery",
    interval=15,
    format="{status} {percentage:.1f}% {remaining:%E%Hh%M}",
    alert=True,
    alert_percentage=15,
    status={"DIS": "", "CHR": "", "FULL": ""},
)


IGNORE_INTERFACES = ["v*", "lo", "br*", "docker*", "tun0"]


status.register(
    NetworkCustom,
    ignore_interfaces=IGNORE_INTERFACES,
    format_up="{bytes_sent:\u2002>5} {bytes_recv:\u2002>5}",
    detect_active=True,
    auto_units=True,
    format_down="",
)

status.register(
    NetworkCustom,
    ignore_interfaces=IGNORE_INTERFACES,
    format_up="{v4}",
    detect_active=True,
    interval=5,
    format_down="",
)

status.register(
    NetworkCustom,
    ignore_interfaces=IGNORE_INTERFACES,
    format_up="{interface}: UP",
    detect_active=True,
    interval=5,
    format_active_up={"w*": "{essid} {quality}%"},
)


status.register("disk", path="/", format=" {avail}G", interval=60)

status.register(
    "mem", format=" {percent_used_mem}%", divisor=1024 ** 3, interval=10)
status.register("swap", format=" {percent_used}%",
                divisor=1024 ** 3, interval=10)

status.register("pulseaudio", format="墳 {volume}%", step=2)

status.register(BacklightCustom, format=" {percentage}%")
status.register(RedshiftManual, format=" {temperature}K", redshift_parameters=[
                "-t", "5700:3500"])


status.run()
