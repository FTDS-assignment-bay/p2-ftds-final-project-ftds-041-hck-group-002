from scripts.extract import extract_data
from scripts.validate import validate_data


def main():

    df = extract_data()

    df, validation = validate_data(df)

    print("\nValidation Summary")
    print("-" * 30)

    for key, value in validation.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()