def check_payment(customer_name, customer_melons, customer_paid):
  """Print customer payment if the amount paid vs the amount expected are not the same."""

  melon_cost = 1.00
  # Calculate the expected cost of the amount of melons purchased
  customer_expected = customer_melons * melon_cost

  # Print a statement if the amount paid does not equal the amount expected
  if customer_expected != customer_paid:
    print(f"{customer_name} paid ${customer_paid:.2f}",
          f"expected ${customer_expected:.2f}"
          )
    # Print whether the user over or underpaid for theri melons
    # If the expected and paid amounts are not the same.
    if customer_expected < customer_paid:
      print(f"{customer_name} overpaid for their melons.")
    elif customer_expected > customer_paid:
      print(f"{customer_name} underpaid for their melons.")

def parse_text_file(file):
  """Open a text file and parse each line to be evaluated by the print_customer_data function."""

  # Open text file
  new_file = open(file)

  # Iterate through each line in the text file
  # Removing trailing white space (\n) from each
  for line in new_file:
    line = line.rstrip()
    # Create a list by splitting the line where "|" occurs
    parsed_line = line.split("|")
    # Unpack the items in the list into appropriate variable names
    count, full_name, customer_melons, customer_paid = parsed_line
    # Only take the first name of the customer name
    customer_name = full_name.split(" ")[0]
    # Check if the customer paid the right amount
    check_payment(customer_name, int(customer_melons), float(customer_paid))

  new_file.close()

def main():
  check_payment("Joe", 5, 5.00)
  check_payment("Frank", 6, 6.00)
  check_payment("Sally", 3, 3.00)
  check_payment("Sean", 9, 9.50)
  check_payment("David", 4, 4.00)
  check_payment("Ashley", 3, 2.00)
  parse_text_file("customer-orders.txt") # Pass text file to be read

main()