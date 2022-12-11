from modules.parser import parser
from modules.extract import ExtractUrl
from modules.convert import write_to_csv


def main():
    args = parser.parse_args()
    
    if args.w:
        ExtractUrl.run(args.w)

if __name__ == "__main__":
    main()