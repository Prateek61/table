import argparse

parser : argparse.ArgumentParser = argparse.ArgumentParser(description='Convert a table in a webpage to sql database')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-w', type=str, nargs='?', help="webpage to extract table from")