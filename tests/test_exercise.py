import pytest
from src.suitcase import Suitcase
from src.item import Item
from src.hold import Hold

def test_exercise(capsys):
    book = Item("The catcher in the rye", 3)
    phone = Item("Nokia 3210", 1)

    assert book.get_name() == "The catcher in the rye"
    assert book.get_weight() == 3

    suitcase = Suitcase(5)
    suitcase.add_item(book)

    assert str(suitcase) == "1 items (3 kg)"

    assert suitcase.heaviest_item() == "Nokia 3210 (1 kg)"

    hold = Hold(1000)
    hold.add_suitcase(suitcase)

    hold.print_items()
    out,err = capsys.readouterr()
    assert "Nokia" in out
