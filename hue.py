import argparse
from bridge import load_config, create_user, save_config
from lights import list_lights, turn_on_off, pick_lights

def main():
    parser = argparse.ArgumentParser(
        description="Control your Philips Hue lights from the terminal.",
        epilog=(
            "Examples:\n"
            "  py-hue list          Show all lights and their current state\n"
            "  py-hue on            Interactively pick lights to turn on\n"
            "  py-hue off           Interactively pick lights to turn off\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subcommands = parser.add_subparsers(dest="command", metavar="command")

    subcommands.add_parser("list", help="List all lights and their state")
    subcommands.add_parser("on", help="Pick and turn on lights that are currently off")
    subcommands.add_parser("off", help="Pick and turn off lights that are currently on")

    # TODO: add a "brightness" subcommand with a --value argument
    # Hint: parser_bri = subcommands.add_parser("brightness")
    #       parser_bri.add_argument("--value", type=int, required=True)

    args = parser.parse_args()
    config = load_config()

    if not config:
        ip = input("Hue bridge IP: ")
        print("Press the button on the bridge, then press Enter...")
        input()
        ip, username = create_user(ip)
        save_config(ip, username)
    else:
        ip, username = config["ip"], config["username"]

    if args.command == "list":
        list_lights(ip, username)
    elif args.command == "on" or args.command == "off":
        light_ids = pick_lights(ip, username, filter="off" if args.command == "on" else "on")
        for id in light_ids:
            turn_on_off(ip, username, id, turn_on=args.command == "on")

if __name__ == "__main__":
    main()