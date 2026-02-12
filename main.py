import sys
import json
from mcstatus import JavaServer

OUTPUT_FILE = "servers.jsonl"

def log(message):
    """Helper function to print to the terminal (stderr) immediately."""
    sys.stderr.write(f"{message}\n")
    sys.stderr.flush()

def scan_server(host, port):
    try:
        address = f"{host}:{port}"
        server = JavaServer.lookup(address)
        status = server.status()
        status_dump = vars(status)

        data = {
            "ip": host,
            "port": port,
            # "version": status.version.name,
            # "players_online": status.players.online,
            # "players_max": status.players.max,
            # "motd": str(status.description),
            "raw_status": status_dump,
        }

        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(data, indent=2, default=str) + "\n")

        log(f"✅ [SUCCESS] {address} is a {status.version.name} server!")

    except Exception as exc:
        log(f"⚠️ [FAIL] {host}:{port} ping failed: {exc}")

if __name__ == "__main__":
    log("🚀 Python Scanner is live and listening for Masscan hits...")
    
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 4 and parts[0] == "open":
            port_found = parts[2]
            host_found = parts[3]
            log(f"🔍 [HIT] Masscan found open port on {host_found}:{port_found}. Pinging...")
            scan_server(host_found, port_found)