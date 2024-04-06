import requests
from dataclasses import dataclass


@dataclass
class Card:
    id: str
    name: str

    def get_image_url(self):
        return f"https://assets.moxfield.net/cards/card-{self.id}-normal.jpg"


class MoxfieldClient:
    baseUrl = "https://api2.moxfield.com/v2/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    def get_deck_by_id(self, deck_id: str):
        print(f"{self.baseUrl}decks/all/{deck_id}")
        response = requests.get(
            f"{self.baseUrl}decks/all/{deck_id}", headers=self.headers
        )

        if response.status_code != 200:
            raise Exception(response.reason)

        body = response.json()
        cards_dictionary = body.get("mainboard", None)

        if cards_dictionary is None:
            raise Exception("Cards not found!")

        cards: list[Card] = []
        for card_name, card_data in cards_dictionary.items():
            card_object = card_data.get("card", None)
            if card_object is None:
                raise Exception("Card body not found!")

            card_id = card_object.get("id", None)
            if card_id is None:
                raise Exception("Card id not found!")

            temp_card = Card(card_id, card_name)
            cards.append(temp_card)

        return cards
