from modules.parser import parser
from modules.extract import table_dict_from_url
from modules.convert import write_to_csv


def main():
    args = parser.parse_args()
    
    if args.w:
        table = table_dict_from_url(args.w)
        write_to_csv(table)

if __name__ == "__main__":
    main()