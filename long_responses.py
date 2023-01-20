import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "You have done your best for today, and tomorrow don't forget to be extraordinary"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Pardon me",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(5)]
    return response
