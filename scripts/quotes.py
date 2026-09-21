import random

# ---------------------------------------------------------
# The Office Quotes Collection
# ---------------------------------------------------------
THE_OFFICE_QUOTES = [
    "“I wanna do a cartwheel. But real casual-like. Not enough to make a big deal out of it, but I know everyone saw it. One stunning, gorgeous cartwheel.” — Creed Bratton",
    "“I’m not superstitious, but I am a little stitious.” — Michael Scott",
    "“I got six numbers. One more and it would have been a complete phone number.” — Kevin Malone",
    "“Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.” — Michael Scott",
    "“The worst thing about prison was the dementors.” — Michael Scott",
    "“I just want to lie on the beach and eat hot dogs. That’s all I’ve ever wanted.” — Kevin Malone",
    "“Oh, you’re paying way too much for worms. Who’s your worm guy?” — Creed Bratton",
    "“Fool me once, strike one. Fool me twice, strike three.” — Michael Scott",
    "“The only problem is whenever I try to make a taco, I get too excited and crush it.” — Kevin Malon",
    "“I guess I’ve been working so hard, I forgot what it’s like to be hardly working.” — Michael Scott",
    "“I don’t hate it. I just don’t like it at all and it’s terrible.” — Michael Scott",
    "“You guys I’m, like, really smart now. You don’t even know. You could ask me, ‘Kelly, what’s the biggest company in the world?’ And I’d be like, ‘blah blah blah, blah blah blah blah blah blah.’ Giving you the exact right answer.” — Kelly Kapoor",
    "“I am a black belt in gift wrapping.” — Jim Halpert",
    "“Who is Justice Beaver?” — Dwight Schrute",
    "“News flash: You are not special.” — Stanley Hudson",
    "“And I knew exactly what to do. But in a much more real sense, I had no idea what to do.” — Michael Scott",
    "“I miss the days when there was only one party I didn’t want to go to.” — Ryan Howard",
    "“Sometimes I get so bored I just want to scream, and then sometimes I actually do scream. I just sort of feel out what the situation calls for.” — Kelly Kapoor",
    "“I am Beyonce, always.” — Michael Scott",
    "“If I can’t scuba, then what’s this all been about? What am I working toward?” — Creed Bratton",
    "“I say dance, they say, ‘How high?'” — Michael Scott",
    "“I wanted to eat a pig in a blanket, in a blanket.” — Kevin Malone",
    "“Tell him to call me ASAP as possible.” — Michael Scott",
    "“I already won the lottery. I was born in the US of A, baby. And as backup, I have a Swiss passport.” — Creed Bratton",
    "“There’s a lot of beauty in ordinary things. Isn’t that kind of the point?” — Pam Beesly",
    "“I’m fast. To give you a reference point. I’m somewhere between a snake and a mongoose. And a panther.” — Dwight Schrute",
    "“There are always a million reasons not to do something.” — Jan Levinson",
    "“It’s a real shame because studies have shown that more information gets passed through water cooler gossip than through official memos. Which puts me at a disadvantage because I bring my own water to work.” — Dwight Schrute",
    "“When Pam gets Michael’s old chair, I get Pam’s old chair. Then I’ll have two chairs. Only one to go.” — Creed Bratton",
    "“I’m always thinking one step ahead, like a carpenter that makes stairs.” — Andy Bernard",
    "“Rit-dit-dit-do-doo!” — Andy Bernard",
    "“Bob Vance, Vance Refrigeration.” — Bob Vance",
]

# ---------------------------------------------------------
# Random Quote Generator
# ---------------------------------------------------------
def get_random_quote():
    """Return a random quote from The Office."""
    quote = random.choice(THE_OFFICE_QUOTES)
    return f"*{quote}*"
