> [!NOTE]
> Have you ever run your own minecraft server scanner??? even if it's run with another scanner.. if you have the data and want to share please contact me at @nandu.fr discord or do a PR to this repo in the server_data folder 

# Minecraft Server Scanner - python
Scans all the Minecraft servers in the internet with default 25565.

- Requires [Masscan](https://github.com/robertdavidgraham/masscan) 
(binary should be at ./masscan/bin/masscan for the below startup cmd to work and the exclude list at ./masscan/data/exclude.conf)
- Requires Python with mcstatus installed.

A small reminder that the [exclude.conf](https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf) file is important, as some IPs should never be scanned, e.g., private network IPs, US government private IPs... scanning them may lead to your ISP getting calls or abuse complaints..

```py
pip install mcstatus
```

# Running the scanner
```sh
sudo ./masscan/bin/masscan 0.0.0.0/0 -p25565 --rate 50000 --excludefile masscan/data/exclude.conf -oL - | python3 main.py
```
`
--rate 50000 can be changed as you wish
`

# Sample result from private runs
- [test_runs](./pinged_servers.jsonl) - 30% on 6th running session, may contain duplicates as the script was shut down and ran about 7 to 9 times for avg 1 to 3 hours