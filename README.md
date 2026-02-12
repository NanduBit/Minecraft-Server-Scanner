# Minecraft Server Scanner - python
Scans all the Minecraft server in the internet with default 25565.

- Requires Masscan
- Requires Python with mcstatus instaled.

```py
pip install mcstatus
```

# Running the scanner
```sh
sudo ./masscan/bin/masscan 0.0.0.0/0 -p25565 --rate 50000 --excludefile masscan/data/exclude.conf -oL - | python3 main.py
```
`
--rate 50000 can be chnages as u wish
`
