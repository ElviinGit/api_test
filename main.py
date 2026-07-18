import argparse
import os

from config.config import get_config

def show_args_kwargs(*args, **kwargs):
    """Example function to show how *args and **kwargs work."""
    print("\nInside show_args_kwargs()")
    print(f"  Positional args (args): {args}")
    print(f"  Keyword args (kwargs): {kwargs}")
    if args:
        print("  Values from args:")
        for i, value in enumerate(args, start=1):
            print(f"    {i}: {value}")
    if kwargs:
        print("  Values from kwargs:")
        for key, value in kwargs.items():
            print(f"    {key}: {value}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect configuration environment")
    parser.add_argument(
        "--env",
        choices=["qa", "stage", "prod"],
        default=os.getenv("TEST_ENV", "qa"),
        help="Environment to use (defaults to TEST_ENV or qa)",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Show a *args/**kwargs demo after printing config",
    )
    args = parser.parse_args()

    config = get_config(args.env)
    print(f"Environment: {config.environment}")
    print(f"Config file: {config.config_path}")
    print("Config values:")
    for key, value in config.get_all().items():
        print(f"  {key}: {value}")

    if args.demo:
        show_args_kwargs("first", "second", env=args.env, debug=True)


if __name__ == "__main__":
    main()
