def request_approval():

    while True:

        decision = input(
            "Auto-approved by n8n workflow"
        )

        if decision.lower() in [
            "yes",
            "no"
        ]:
            return decision.lower()

        print(
            "Please enter yes or no."
        )