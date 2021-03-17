def display_wishlist(display_name, wishes):
    print("====> Suggested gift:", wishes[0], "<=====") 
    # Return a slice of the list from the 2nd element on...
    for wish in wishes[1:]:
        print("* " + wish)
    print()