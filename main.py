import sys
import json
import socket
from mcstatus import JavaServer

OUTPUT_FILE = "pinged_servers.jsonl"
TIMEOUT = 10  # seconds

def log(message):
    """Helper function to print to the terminal (stderr) immediately."""
    sys.stderr.write(f"{message}\n")
    sys.stderr.flush()

def scan_server(host, port):
    try:
        # Set socket timeout to allow enough time for server response
        socket.setdefaulttimeout(TIMEOUT)
        
        address = f"{host}:{port}"
        server = JavaServer.lookup(address)
        status = server.status()
        
        # try:
        #     query_data = server.query()
        #     print(query_data)
        # except Exception as query_exc:
        #     log(f"   ⚠️ Query failed (non-critical): {query_exc}")
        
        status_dump = vars(status)

        data = {
            "ip": host,
            "port": port,
            "version": status.version.name,
            "motd": str(status.description),
            "ping": float(status.latency),
            "players_online": status.players.online,
            "players_max": status.players.max,
            "sample_players": status.players.sample,
            "enforces_secure_chat": status.enforces_secure_chat,
            "icon": status.icon,
            "forge_data": status.forge_data,
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
