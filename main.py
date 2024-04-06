import argparse
from moxfield import MoxfieldClient
from image_generate import generate_image
from InquirerPy import inquirer


def main(args):
    client = MoxfieldClient()
    decks = client.get_decks_by_user(args.user_id)
    selectedDecks = inquirer.select(
        message="Select decks:", choices=decks,
        multiselect=True
    ).execute()

    for deck_id, deck_name in selectedDecks:
        print(f"deck: {deck_id}, {deck_name}")
        deck = client.get_deck_by_id(deck_id)
        images = list(map(lambda x: x.get_image_url(), deck))
        generate_image(images, (4, 3), deck_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_id", help="an id for moxfield users")
    args = parser.parse_args()
    main(args)
