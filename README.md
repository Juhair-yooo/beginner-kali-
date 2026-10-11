# kali-cmd-finder

Type what you want to do, get the command for it. A searchable reference for common Kali Linux tools and commands — no more trying to remember whether it's `-sV` or `-sS`.

## Usage
# interactive mode 
process 

unzip kali-cmd-finder.zip && cd kali-cmd-finder
git init
git add .
git commit -m "Initial commit: Kali command finder"
# create an empty repo on github.com first, then:
git remote add origin https://github.com/<your-username>/kali-cmd-finder.git
git branch -M main
git push -u origin main
```bash
# interactive mode
python3 search.py

# one-shot query
python3 search.py "scan ports"
python3 search.py "crack a hash"
python3 search.py "wifi"
process 

unzip kali-cmd-finder.zip && cd kali-cmd-finder
git init
git add .
git commit -m "Initial commit: Kali command finder"
# create an empty repo on github.com first, then:
git remote add origin https://github.com/<your-username>/kali-cmd-finder.git
git branch -M main
git push -u origin main
```

Example:

```
$ python3 search.py "scan ports"

=== nmap  [Recon] ===
Port and service scanning
  $ nmap -sV -O <target>
    -> Scan ports, detect service versions and OS
  $ nmap -sC -sV -p- <target>
    -> Default scripts, scan all 65535 ports
  ...
```

No dependencies — just Python 3 and the standard library.

## What's covered

Recon, vulnerability analysis, password attacks, wireless, exploitation, sniffing/forensics, reverse engineering, social engineering, and general-purpose Linux/networking commands. Run `categories` inside interactive mode to see the full list.

## Adding your own commands

All data lives in [`commands.json`](commands.json). Each entry looks like:

```json
{
  "tool": "nmap",
  "category": "Recon",
  "description": "Port and service scanning",
  "keywords": ["scan", "port scan", "service detection"],
  "commands": [
    {"cmd": "nmap -sV -O <target>", "desc": "Scan ports, detect service versions and OS"}
  ]
}
```

Add a new object to the array and it's immediately searchable — no code changes needed.

## Legal / ethical use

These tools are for systems you own or are explicitly authorized to test — your own labs, VMs, or platforms like HackTheBox / TryHackMe / DVWA. Unauthorized use against systems you don't control is illegal in most jurisdictions.

## License

MIT — see [LICENSE](LICENSE).
