def get_localized_sizes(size_input, country_input):
    sizes_mapping = {
        "S": {"Ukraine": 46, "Germany": 40, "USA": 12, "France": 42, "UK": 28},
        "M": {"Ukraine": 48, "Germany": 42, "USA": 14, "France": 44, "UK": 30},
        "L": {"Ukraine": 50, "Germany": 44, "USA": 16, "France": 46, "UK": 32},

    }
    # if size_input == "S" and country_input == "USA":
    #    print("Domestic Sizes of S:", sizes_mapping["S"]["USA"])
    if size_input in sizes_mapping and country_input in sizes_mapping[size_input]:
        print(f"Domestic Sizes of {size_input}: {sizes_mapping[size_input][country_input]}")


def main():
    while True:
        size_input = str(input("Enter the international size (S, M or L):")).upper()
        if size_input in ["S", "M", "L"]:
            break
        else:
            print("Invalid input. Please enter only international sizes: S, M or L")

    while True:
        country_input = str(input("Enter the country (Ukraine, Germany, USA, France, UK):")).capitalize()
        if country_input in ["Ukraine", "Germany", "USA", "France", "UK"]:
            get_localized_sizes(size_input, country_input)
            break
        else:
            print("Invalid input. Please enter valid country:")


main()
