import requests
from dataclasses import dataclass


@dataclass
class Card:
    id: str
    name: str
    
    def get_image_url():
        return f"https://assets.moxfield.net/cards/card-{id}-normal.jpg"


class MoxfieldClient:
    baseUrl = "https://api2.moxfield.com/v2/"

    def get_deck_by_id(self, deck_id: str):
        response = requests.get(f"{self.baseUrl}decks/all/{deck_id}")

        if response.status_code != 200:
            raise Exception("Deck not found!")

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
