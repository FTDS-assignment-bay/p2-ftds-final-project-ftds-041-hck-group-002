from scripts.extract import extract_data
from scripts.validate import validate_data
from scripts.clean import clean_data


def main():

    df = extract_data()

    df, validation = validate_data(df)

    df = clean_data(df)

    print(df.info())

    print()

    print(df.describe())


if __name__ == "__main__":
    main()