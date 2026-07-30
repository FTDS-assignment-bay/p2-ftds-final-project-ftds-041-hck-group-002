from scripts.extract import extract_data


def main():

    df = extract_data()

    print(df.head())

    print()

    print(df.shape)


if __name__ == "__main__":
    main()