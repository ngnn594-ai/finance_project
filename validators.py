from datetime import datetime
from logger import logger


def validate_amount(args):
    if args.amount <= 0:
        logger.error(f"Invalid amount: {args.amount}")
        raise ValueError("Сумма должна быть больше 0")


def validate_category(args):
    if not args.category or not args.category.strip():
        logger.error("Invalid category (empty)")
        raise ValueError("Категория не должна быть пустой")


def validate_date(date_str):
    if not date_str or not date_str.strip():
        logger.error("Empty date")
        raise ValueError("Дата не должна быть пустой")

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        logger.error(f"Invalid date format: {date_str}")
        raise ValueError("Некорректный формат даты (YYYY-MM-DD)")


def validate_comment(args):
    if not args.comment or not args.comment.strip():
        logger.error("Invalid comment (empty)")
        raise ValueError("Описание не должно быть пустым")


def validate_currency(args):
    if not args.currency or len(args.currency) != 3:
        logger.error(f"Invalid currency: {args.currency}")
        raise ValueError("Валюта должна быть 3 буквы (например USD)")


def validate_type(args):
    if args.type not in ["expense", "income"]:
        logger.error(f"Invalid type: {args.type}")
        raise ValueError("type должен быть income или expense")



def validate_all(args):
    validate_comment(args)
    validate_amount(args)
    validate_category(args)
    validate_date(args.date)
    validate_currency(args)
    validate_type(args)