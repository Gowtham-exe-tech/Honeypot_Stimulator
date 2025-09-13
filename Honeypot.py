import socket
import datetime

# Configuration
HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 2222        # Fake SSH port
LOG_FILE = "honeypot_log.txt"
RECV_BUFFER = 2048
CLIENT_TIMEOUT = 3  # seconds: short timeout to decide client finished typing

def now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_event(message):
    """Automatically timestamped logging (file + stdout)."""
    line = f"[{now_str()}] {message}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # allow quick restarts
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    log_event(f"[STARTED] Honeypot running on port {PORT}...")

    try:
        while True:
            try:
                conn, addr = server.accept()
            except KeyboardInterrupt:
                raise
            ip, port = addr
            log_event(f"Connection from {ip}:{port}")

            # Send fake SSH banner
            banner = "SSH-2.0-OpenSSH_8.2\r\n"
            try:
                conn.sendall(banner.encode())
            except Exception as e:
                log_event(f"[ERROR] Sending banner to {ip}:{port} -> {e}")
                conn.close()
                continue

            # collect data until client closes or timeout
            conn.settimeout(CLIENT_TIMEOUT)
            buffer_parts = []
            try:
                while True:
                    chunk = conn.recv(RECV_BUFFER)
                    if not chunk:
                        # client closed connection
                        break
                    # keep raw chunk (ignore decode errors)
                    try:
                        text = chunk.decode(errors="ignore")
                    except Exception:
                        text = ""
                    if text:
                        buffer_parts.append(text)
                    # if chunk contains newline, keep reading a short time for more input
                    # (we still rely on timeout to stop eventually)
            except socket.timeout:
                # no more data from client within timeout -> treat as end
                pass
            except Exception as e:
                log_event(f"[ERROR] Receiving from {ip}:{port} -> {e}")

            # join and normalize input
            if buffer_parts:
                full = "".join(buffer_parts)
                # split into lines to log meaningful pieces (username/password typed on separate lines)
                # strip trailing control chars
                lines = [ln.strip() for ln in full.splitlines() if ln.strip() != ""]
                if lines:
                    for ln in lines:
                        log_event(f"Input from {ip}:{port}: {ln}")
                else:
                    # if no newline-separated lines, log raw captured data trimmed
                    trimmed = full.strip()
                    if trimmed:
                        log_event(f"Input from {ip}:{port}: {trimmed}")
            else:
                log_event(f"No input captured from {ip}:{port}")

            conn.close()
            log_event(f"Closed connection {ip}:{port}")

    except KeyboardInterrupt:
        log_event("KeyboardInterrupt received — shutting down honeypot.")
    except Exception as e:
        log_event(f"[FATAL] {e}")
    finally:
        try:
            server.close()
        except Exception:
            pass
        log_event("[STOPPED] Honeypot stopped")

if __name__ == "__main__":
    start_honeypot()
