from flask import render_template, session


INITIAL_MENU = {"CandyBar": 200, "Chips": 150, "Soda": 100}
AVAILABLE_COINS = [5, 10, 25, 100, 200]


def index():
    return render_template("main.html", menu=INITIAL_MENU, available_coins=AVAILABLE_COINS,)


def process_order(selected_item: str, inserted_amount: int):
    session["inserted_amount"] = inserted_amount

    if inserted_amount >= INITIAL_MENU[selected_item]:
        change = inserted_amount - INITIAL_MENU[selected_item]
        template = "success.html"
    else:
        change = 0
        template = "process.html"

    return render_template(template, available_coins=AVAILABLE_COINS,
                           inserted_amount=inserted_amount, selected_item=selected_item, change=change)


def cancel_order():
    inserted_amount = session["inserted_amount"]
    session.clear()
    return render_template("cancel.html", inserted_amount=inserted_amount)
