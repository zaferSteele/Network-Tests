# Zafer Steele's Network Test toolkit

**Network-Tests** is a collection of cross-platform Python scripts designed to test and monitor network connectivity. It includes tools for:

* Pinging hosts (basic or detailed)
* Measuring round-trip latency
* Checking host reachability across OS types
* Performing lightweight diagnostics

---

## Features

### ✅ Cross-Platform Latency Checks

* `cross_platform_ping.py`: Uses `subprocess` and regex parsing to get RTT and reachability from `ping`.
* Automatically detects the correct ping flag (`-n` for Windows, `-c` for Unix).

### 🌐 Reachability Tests

* `ping_test_using_os_module.py`: Uses `os.system()` to check host response (prints result directly).
* `ping_test_using_subprocess.py`: Uses `subprocess.Popen()` to execute ping and returns results.

---

## Installation

```bash
# Clone the repo
$ git clone https://github.com/zaferSteele/Network-Tests.git
$ cd Network-Tests

# (Optional) Create and activate a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate
```

> No external packages required — only built-in Python modules are used.

---

## Usage

### 1. Cross Platform Ping with Output Parsing

```bash
$ python "network latency tests/cross_platform_ping.py"
```

### 2. Reachability with os.system()

```bash
$ python "network reachability tests/ping_test_using_os_module.py"
```

### 3. Reachability with subprocess.Popen()

```bash
$ python "network reachability tests/ping_test_using_subprocess.py"
```

---

## Output Example

```bash
[('www.juniper.com', 'time=20.1 ms'), ('www.google.com', 'time=14.7 ms')]
```

---

## Project Structure

```
network latency tests/
├── cross_platform_ping.py
├── ping_hosts_only_for_unix_platforms.py

network reachability tests/
├── ping_test_using_os_module.py
└── ping_test_using_subprocess.py
```

## 👤 Author

**Zafer Steele**
GitHub: [@zaferSteele](https://github.com/zaferSteele)

---

## 📝 License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

