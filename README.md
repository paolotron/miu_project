# MIU Project
MIU solver from "gödel escher bach an eternal golden braid" book.
The implemented algorithm is a simple [A star search](https://en.wikipedia.org/wiki/A*_search_algorithm) that uses
the [leveshtein distance](https://en.wikipedia.org/wiki/A*_search_algorithm) as metric.
Unfortunately the given problem can be [demostrated to be impossible](https://en.wikipedia.org/wiki/MU_puzzle), nontheless the algorithm can be used
on other systems by simply modifying the config file

## System definition
Write in the .yaml file the starting and ending points using the *start* and *end* tag
```yaml
  start: MI
  end: MU
```
and report the list of rules of the system in regex format using the *rules* tag:
```yaml
rules:
  "I$": "IU"
  "M(.*)$": "M\\1\\1"
  "III": "U"
  "UU": "U"
```
For defining *x* patterns use regex groups like in the example
## Usage
Simply run
```
  python miu_project.py rules.yaml
```
