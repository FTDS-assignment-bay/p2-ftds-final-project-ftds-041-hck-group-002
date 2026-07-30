from scripts.extract import extract_data
from scripts.validate import validate_data
from scripts.clean import clean_data
from scripts.transform import transform_data
from scripts.load import load_dataframe


def main():

    # Extract
    df = extract_data()

    # Validate
    df, _ = validate_data(df)

    # Clean
    df = clean_data(df)

    # Transform
    df = transform_data(df)

    # Load ke analytics
    load_dataframe(
        dataframe=df,
        schema="analytics",
        table="sales",
        if_exists="replace"
    )


if __name__ == "__main__":
    main()