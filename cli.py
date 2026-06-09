import argparse
from services import add_transaction, export_to_csv,import_data_csv , filter_transactions
from logger import logger
from validators import validate_all
from report import get_stats , print_transactions , print_top_categories


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add" ,help="адд нью трансакшен (инкам  ор экспенс)")
add_parser.add_argument("--amount", type=float, required=True)
add_parser.add_argument("--category", type=str, required=True)
add_parser.add_argument("--date", type=str, required=True)
add_parser.add_argument("--comment", type=str, required=True)
add_parser.add_argument("--currency", type=str, required=True)
add_parser.add_argument("--type", type=str, required=True)


import_parser = subparsers.add_parser("import_csv")
import_parser.add_argument("--path", type=str, required=True)


list_parser = subparsers.add_parser("list")

list_parser.add_argument("--type", type=str, required=False)
list_parser.add_argument("--category", type=str, required=False)
list_parser.add_argument("--start", type=str, required=False)
list_parser.add_argument("--end", type=str, required=False)


subparsers.add_parser("stats")
subparsers.add_parser("top_categories")
subparsers.add_parser("export_csv")

args = parser.parse_args()
logger.info(f"Command: {args.command}")



if args.command == "add":

    validate_all(args)
    add_transaction(args)

elif args.command == "list":

    list_stat = filter_transactions(
        tx_type=args.type,
        category=args.category,
        start_date=args.start,
        end_date=args.end
    )
    print_transactions(list_stat)



elif args.command == "stats":
    get_stats()

elif args.command == "top_categories":
    print_top_categories()

elif args.command == "export_csv":
     export_to_csv()

elif args.command == "import_csv":
    import_data_csv(args.path)