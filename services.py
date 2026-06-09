from storage import load_data, save_data
from logger import logger
from pathlib import Path
import csv
from logger import logger, log_call

def get_next_id(data):
    return max((item["id"] for item in data), default=0) + 1

@log_call
def add_transaction(args):


    data = load_data()

    new_id = get_next_id(data)

    record = {
        "id": new_id,
        "type": args.type,
        "amount": args.amount,
        "category": args.category,
        "date": args.date,
        "currency": args.currency,
        "comment": args.comment

    }

    data.append(record)
    save_data(data)

    logger.info(
        f"Transaction added: id={record['id']}, "
        f"type={record['type']}, "
        f"amount={record['amount']}, "
        f"category={record['category']}"
    )




@log_call
def export_to_csv():
    data = load_data()
    if not data:
        raise ValueError("No data to export")

    logger.info(f"Export started: {len(data)} records")
    with open('data/data.csv', "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())

        writer.writeheader()

        for row in data:
            writer.writerow(row)

    logger.info("Export finished")

@log_call
def import_data_csv(path):

    file = Path("data") / path
    print(file)
    if not file.exists():
        logger.error(f"File not found: {path}")
        print("Ошибка: файл не существует")
        return

    logger.info(f"Import started: {path}")


    new_records = []
    data = load_data()
    next_id = get_next_id(data)

    for row in read_csv_stream(file):
        try:
            new_records.append({
                "id": next_id,
                "type": row["type"],
                "amount": float(row["amount"] or 0),
                "category": row["category"],
                "date": row["date"],
                "comment": row["comment"]
            })
            next_id += 1
        except Exception as e:
            logger.error(f"Bad row skipped: {row} | error: {e}")

    data.extend(new_records)
    save_data(data)

@log_call
def filter_transactions(tx_type=None, category=None, start_date=None, end_date=None):
    data = load_data()
    result = []


    for item in data:

        if  tx_type and item.get("type") != tx_type:
            continue

        if category and item.get("category") != category:
            continue

        if start_date and item.get("date") < start_date:
            continue

        if end_date and item.get("date") > end_date:
            continue

        result.append(item)

    return result


def read_csv_stream(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
