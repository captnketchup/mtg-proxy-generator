import argparse
from moxfield import MoxfieldClient
from image_generate import generate_image


def main(args):
    client = MoxfieldClient()
    deck = client.get_deck_by_id(args.deck_id)
    images = list(map(lambda x: x.get_image_url(), deck))
    generate_image(images, (4, 3), args.deck_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deck_id", help="an id for moxfield decks")
    args = parser.parse_args()
    main(args)
