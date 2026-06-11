def request_approval():

    while True:

        decision = input(
            "\nApprove Travel Plan? (yes/no): "
        )

        if decision.lower() in [
            "yes",
            "no"
        ]:
            return decision.lower()

        print(
            "Please enter yes or no."
        )