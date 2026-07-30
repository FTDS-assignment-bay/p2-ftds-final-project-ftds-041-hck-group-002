from scripts.extract import extract_data
from scripts.validate import validate_data
from scripts.clean import clean_data
from scripts.transform import transform_data


def main():

    # Extract
    df = extract_data()

    # Validate
    df, validation = validate_data(df)

    # Clean
    df = clean_data(df)

    # Transform
    df = transform_data(df)

    print("\nNew Features")
    print("-" * 50)

    print(
        df[
            [
                "date",
                "year",
                "month",
                "quarter",
                "week_of_year",
                "day_of_week",
                "weekend_flag",
                "revenue",
            ]
        ].head()
    )

    print("\nDataFrame Summary")
    print("-" * 50)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns")
    print("-" * 50)

    for column in df.columns:
        print(column)


if __name__ == "__main__":
    main()