from scripts.extract import extract_data
from scripts.load import load_dataframe


def main():

    df = extract_data()

    load_dataframe(
        dataframe=df,
        schema="raw",
        table="sales",
    )


if __name__ == "__main__":
    main()